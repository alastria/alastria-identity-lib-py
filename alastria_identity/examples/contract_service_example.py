import os

from web3 import Web3

from alastria_identity.services import (
    ContractsService, IdentityConfigBuilder, ContractParser)


def main():
    # We generate the config based on the markdown
    CONTRACTS_INFO_URL = 'https://raw.githubusercontent.com/alastria/alastria-identity/master/contracts/ContractInfo.md'
    builder = IdentityConfigBuilder(
        contracts_info_url=CONTRACTS_INFO_URL,
        parser_class=ContractParser
    )
    config = builder.generate()

    # We instantiate the contract service
    ALASTRIA_IDENTITY_MANAGER_CONTRACT_NAME = 'AlastriaIdentityManager'
    PROVIDER_NODE_URL = os.environ.get(
        'PROVIDER_NODE_URL', 'https://127.0.0.1/rpc')

    endpoint = Web3(Web3.HTTPProvider(PROVIDER_NODE_URL))

    contract_service = ContractsService(config)
    alastria_identity_manager_contract = contract_service.get_contract_handler(
        ALASTRIA_IDENTITY_MANAGER_CONTRACT_NAME, endpoint)


if __name__ == '__main__':
    main()
