""" Private class, that should tell me if given account type is of asset or liability.  Example SBA account type is asset & EMI, CCMAIN, CONS_LOAN are liabilities.
Remember SBA,EMI,etc are just examples.
"""


class AccountClassifier:
    _asset_accounts = {"SBA", "SAV", "FD", "MF"}  # Example asset account types
    _liability_accounts = {
        "EMI",
        "CCMAIN",
        "CONS_LOAN",
    }  # Example liability account types

    _attributes_sets = {
        "SBA": set(),
        "SAV": set(),
        "FD": set(),
        "MF": set(),
        "EMI": {"emi_amount", "emi_due_count"},
        "CCMAIN": {"total_due"},
        "CONS_LOAN": set(),
    }

    @staticmethod
    def _is_asset(account_type: str) -> bool:
        return account_type in AccountClassifier._asset_accounts

    @staticmethod
    def _is_liability(account_type: str) -> bool:
        return account_type in AccountClassifier._liability_accounts

    @classmethod
    def get_account_category(cls, account_type: str) -> str:
        """returns 'asset' or 'liability' str"""
        if cls._is_asset(account_type):
            return "asset"
        elif cls._is_liability(account_type):
            return "liability"
        else:
            return "unknown"

    @classmethod
    def get_attributes_set(cls, account_type: str) -> set:
        return cls._attributes_sets.get(account_type, set())
