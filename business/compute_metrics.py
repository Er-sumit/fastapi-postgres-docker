from business.definitions.AccountClassifier import AccountClassifier
from core.config import log
from db.repository.account import list_accounts


def get_asset_value(account):
    log.info(f"get_asset_value method received arg of type {type(account)}")
    log.info(f"looking for asset value in {account}")
    return account.available_bal


def get_liability_values(account):
    total_liabilities_value = 0
    log.info(
        f"adding liabilities values from account = {account.type} - {account.title}"
    )
    for account_liability_attribute in AccountClassifier.get_attributes_set(
        account.type
    ):
        if account_liability_attribute == "total_due":
            total_liabilities_value += account.total_due
        elif account_liability_attribute == "emi_amount":
            total_liabilities_value += account.emi_amount * account.emi_due_count
        elif account_liability_attribute == "emi_due_count":
            pass
        else:
            pass
    return total_liabilities_value


def total_assets(db, tenure="whole_future"):
    grand_total = sum(
        [
            get_asset_value(account)
            for account in list_accounts(db=db)
            if AccountClassifier.get_account_category(str(account.type)) == "asset"
        ]
    )
    log.info(f"Total assets value is {grand_total}")
    return grand_total


def total_liabilities(db, tenure="whole_future"):
    grand_total = sum(
        [
            get_liability_values(account)
            for account in list_accounts(db=db)
            if AccountClassifier.get_account_category(str(account.type)) == "liability"
        ]
    )
    return grand_total


def months_liability_value(account, the_month=0):
    total_liabilities_value = 0
    log.info(
        f"adding liabilities values from account = {account.type} - {account.title}"
    )
    for account_liability_attribute in AccountClassifier.get_attributes_set(
        account.type
    ):
        if account_liability_attribute == "total_due" and the_month == 0:
            total_liabilities_value += account.billed_due
        elif account_liability_attribute == "total_due" and the_month == 1:
            total_liabilities_value += account.unbilled_due
        elif (
            account_liability_attribute == "emi_amount"
            and the_month + 1 <= account.emi_due_count
        ):
            total_liabilities_value += account.emi_amount
        elif account_liability_attribute == "emi_due_count":
            pass
        else:
            pass
    return total_liabilities_value


def get_monthly_liability_values(account, n=1):
    monthly_dict = {"account_title": account.title}
    # monthly_details_dict = [ {i:[]} for i in range(n)]

    for curr_month_count in range(n):
        monthly_dict[f"plus_{curr_month_count}_month"] = months_liability_value(
            account, the_month=curr_month_count
        )
        # monthly_details_dict[curr_month_count][curr_month_count].append({account.title: []})
    # return {"account_title": account.title, "plus_0_month": value, "plus_1_month": value, "plus_2_month": value }
    return monthly_dict


def liabilities_near_qtr(db, tenure="whole_future"):
    """should return liabilities dict as {"plus_0_month": value, "plus_1_month": value, "plus_2_month": value }"""
    monthly_data = [
        get_monthly_liability_values(account, n=3)
        for account in list_accounts(db=db)
        if AccountClassifier.get_account_category(str(account.type)) == "liability"
    ]
    # monthly_data =  [{"account_title": "account_title_1", "plus_0_month": value, "plus_1_month": value, "plus_2_month": value },{"account_title": "account_title_2","plus_0_month": value, "plus_1_month": value, "plus_2_month": value }]
    log.info(f"monthly_details: {monthly_data}")
    account_wise_details = [{data.get("account_title"): data} for data in monthly_data]
    log.info(f"Account wise details = {account_wise_details}")
    return_dict = {}
    for n in range(3):
        return_dict[f"plus_{n}_month"] = sum(
            [data.get(f"plus_{n}_month", 0) for data in monthly_data]
        )
    return_dict["account_wise_details"] = account_wise_details
    # adding monthly-account-wise details
    monthly_account_wise_data = [{f"plus_{n}_month": []} for n in range(3)]
    for account in account_wise_details:
        for num in range(3):
            account_title = list(account.keys())[-1]
            monthly_account_wise_data[num].get(f"plus_{num}_month").append(
                {account_title: account[account_title].get(f"plus_{num}_month", 0)}
            )
            log.info(
                f"appending {account[account_title].get(f'plus_{num}_month',0)} to month {num} for account {account_title} "
            )
    return_dict["monthly_account_wise_data"] = monthly_account_wise_data
    return return_dict

def total_cash(db, tenure="whole_future"):
    values_list = [
        get_asset_value(account)
        for account in list_accounts(db=db)
        if account.type == "SBA"
    ]
    grand_total = sum(
        values_list
    )
    return grand_total