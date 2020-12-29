from web3 import Web3
from web3.contract import Contract

IDENTITY_MANAGER_ADDRESS = '0xbd4a2c84edb97be5beff7cd341bd63567e73f8c9'

class ContractsService:
    @staticmethod
    def AlastriaIdentityEntity(endpoint: Web3) -> Contract:
        # TODO get the ABI from autogenerated config
        return endpoint.eth.contract(
            abi=[{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"constant":False,"inputs":[{"internalType":"address","name":"_addressEntity","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_cif","type":"string"},{"internalType":"string","name":"_url_logo","type":"string"},{"internalType":"string","name":"_url_createAID","type":"string"},{"internalType":"string","name":"_url_AOA","type":"string"},{"internalType":"bool","name":"_active","type":"bool"}],"name":"addEntity","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_addressEntity","type":"address"},{"internalType":"string","name":"_name","type":"string"}],"name":"setNameEntity","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_addressEntity","type":"address"},{"internalType":"string","name":"_cif","type":"string"}],"name":"setCifEntity","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_addressEntity","type":"address"},{"internalType":"string","name":"_url_logo","type":"string"}],"name":"setUrlLogo","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_addressEntity","type":"address"},{"internalType":"string","name":"_url_createAID","type":"string"}],"name":"setUrlCreateAID","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_addressEntity","type":"address"},{"internalType":"string","name":"_url_AOA","type":"string"}],"name":"setUrlAOA","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_addressEntity","type":"address"}],"name":"getEntity","outputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_cif","type":"string"},{"internalType":"string","name":"_url_logo","type":"string"},{"internalType":"string","name":"_url_createAID","type":"string"},{"internalType":"string","name":"_url_AOA","type":"string"},{"internalType":"bool","name":"_active","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"entitiesList","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":False,"stateMutability":"view","type":"function"}]
        )

    @staticmethod
    def AlastriaIdentityManager(endpoint: Web3) -> Contract:
        # TODO get the ABI from autogenerated config
        return endpoint.eth.contract(
            abi=[{"constant":True,"inputs":[{"name":"","type":"address"}],"name":"identityKeys","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_identityIssuer","type":"address"}],"name":"getEidasLevel","outputs":[{"name":"","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_identityServiceProvider","type":"address"}],"name":"addIdentityServiceProvider","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_addressEntity","type":"address"},{"name":"_url_logo","type":"string"}],"name":"setUrlLogo","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"newOwner","type":"address"}],"name":"transfer","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_addressEntity","type":"address"},{"name":"_cif","type":"string"}],"name":"setCifEntity","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"}],"name":"pendingIDs","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"addr","type":"address"}],"name":"isOwner","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_identityServiceProvider","type":"address"}],"name":"deleteIdentityServiceProvider","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"alastriaPresentationRegistry","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_identityIssuer","type":"address"},{"name":"_level","type":"uint8"}],"name":"updateIdentityIssuerEidasLevel","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_signAddress","type":"address"}],"name":"prepareAlastriaID","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_addressEntity","type":"address"},{"name":"_url_createAID","type":"string"}],"name":"setUrlCreateAID","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"version","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_destination","type":"address"},{"name":"_value","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"delegateCall","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_identityIssuer","type":"address"}],"name":"isIdentityIssuer","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"addPublicKeyCallData","type":"bytes"}],"name":"createAlastriaIdentity","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"entitiesList","outputs":[{"name":"","type":"address[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_addressEntity","type":"address"}],"name":"getEntity","outputs":[{"name":"_name","type":"string"},{"name":"_cif","type":"string"},{"name":"_url_logo","type":"string"},{"name":"_url_createAID","type":"string"},{"name":"_url_AOA","type":"string"},{"name":"_active","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_identityIssuer","type":"address"},{"name":"_level","type":"uint8"}],"name":"addIdentityIssuer","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_addressEntity","type":"address"},{"name":"_url_AOA","type":"string"}],"name":"setUrlAOA","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_addressEntity","type":"address"},{"name":"_name","type":"string"},{"name":"_cif","type":"string"},{"name":"_url_logo","type":"string"},{"name":"_url_createAID","type":"string"},{"name":"_url_AOA","type":"string"},{"name":"_active","type":"bool"}],"name":"addEntity","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"accountLost","type":"address"},{"name":"newAccount","type":"address"}],"name":"recoverAccount","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_identityIssuer","type":"address"}],"name":"deleteIdentityIssuer","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_identityServiceProvider","type":"address"}],"name":"isIdentityServiceProvider","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"alastriaCredentialRegistry","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_addressEntity","type":"address"},{"name":"_name","type":"string"}],"name":"setNameEntity","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"alastriaPublicKeyRegistry","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_version","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"name":"signAddress","type":"address"}],"name":"PreparedAlastriaID","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"method","type":"string"}],"name":"OperationWasNotSupported","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"identity","type":"address"},{"indexed":True,"name":"creator","type":"address"},{"indexed":False,"name":"owner","type":"address"}],"name":"IdentityCreated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"oldAccount","type":"address"},{"indexed":False,"name":"newAccount","type":"address"},{"indexed":True,"name":"serviceProvider","type":"address"}],"name":"IdentityRecovered","type":"event"}]
        )

    @staticmethod
    def AlastriaPublicKeyRegistry(endpoint: Web3) -> Contract:
        # TODO get the ABI from autogenerated config
        return endpoint.eth.contract(
            abi=[{"constant":True,"inputs":[{"name":"subject","type":"address"},{"name":"publicKey","type":"bytes32"}],"name":"getPublicKeyStatus","outputs":[{"name":"exists","type":"bool"},{"name":"status","type":"uint8"},{"name":"startDate","type":"uint256"},{"name":"endDate","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"subject","type":"address"}],"name":"getCurrentPublicKey","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"publicKey","type":"string"}],"name":"deletePublicKey","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"publicKey","type":"string"}],"name":"addKey","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"version","outputs":[{"name":"","type":"int256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"previousPublishedVersion","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"publicKeyList","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"publicKey","type":"string"}],"name":"revokePublicKey","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_previousPublishedVersion","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"name":"publicKey","type":"string"}],"name":"PublicKeyDeleted","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"publicKey","type":"string"}],"name":"PublicKeyRevoked","type":"event"}]
        )

    @staticmethod
    def AlastriaCredentialRegistry(endpoint: Web3) -> Contract:
        # TODO get the ABI from autogenerated config
        return endpoint.eth.contract(
            abi=[{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"issuerCredentialList","outputs":[{"name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"subject","type":"address"}],"name":"getSubjectCredentialList","outputs":[{"name":"","type":"uint256"},{"name":"","type":"bytes32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"version","outputs":[{"name":"","type":"int256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"subject","type":"address"},{"name":"subjectCredentialHash","type":"bytes32"}],"name":"getSubjectCredentialStatus","outputs":[{"name":"exists","type":"bool"},{"name":"status","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"subjectStatus","type":"uint8"},{"name":"issuerStatus","type":"uint8"}],"name":"getCredentialStatus","outputs":[{"name":"","type":"uint8"}],"payable":False,"stateMutability":"pure","type":"function"},{"constant":True,"inputs":[],"name":"previousPublishedVersion","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"bytes32"}],"name":"subjectCredentialRegistry","outputs":[{"name":"exists","type":"bool"},{"name":"status","type":"uint8"},{"name":"URI","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"issuer","type":"address"},{"name":"issuerCredentialHash","type":"bytes32"}],"name":"getIssuerCredentialStatus","outputs":[{"name":"exists","type":"bool"},{"name":"status","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"subjectCredentialList","outputs":[{"name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"issuerCredentialHash","type":"bytes32"}],"name":"addIssuerCredential","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"issuerCredentialHash","type":"bytes32"},{"name":"status","type":"uint8"}],"name":"updateCredentialStatus","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"subjectCredentialHash","type":"bytes32"}],"name":"deleteSubjectCredential","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"subjectCredentialHash","type":"bytes32"},{"name":"URI","type":"string"}],"name":"addSubjectCredential","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_previousPublishedVersion","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"name":"subjectCredentialHash","type":"bytes32"}],"name":"SubjectCredentialDeleted","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"issuerCredentialHash","type":"bytes32"},{"indexed":False,"name":"status","type":"uint8"}],"name":"IssuerCredentialRevoked","type":"event"}]
        )

    @staticmethod
    def AlastriaPresentationRegistry(endpoint: Web3) -> Contract:
        # TODO get the ABI from autogenerated config
        return endpoint.eth.contract(
            abi=[{"constant":True,"inputs":[{"name":"subjectStatus","type":"uint8"},{"name":"receiverStatus","type":"uint8"}],"name":"getPresentationStatus","outputs":[{"name":"","type":"uint8"}],"payable":False,"stateMutability":"pure","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"bytes32"}],"name":"subjectPresentationRegistry","outputs":[{"name":"exists","type":"bool"},{"name":"status","type":"uint8"},{"name":"URI","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"receiverPresentationHash","type":"bytes32"},{"name":"status","type":"uint8"}],"name":"updateReceiverPresentation","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"subjectPresentationHash","type":"bytes32"},{"name":"URI","type":"string"}],"name":"addSubjectPresentation","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"subject","type":"address"},{"name":"subjectPresentationHash","type":"bytes32"}],"name":"getSubjectPresentationStatus","outputs":[{"name":"exists","type":"bool"},{"name":"status","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"version","outputs":[{"name":"","type":"int256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"previousPublishedVersion","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"receiver","type":"address"},{"name":"receiverPresentationHash","type":"bytes32"}],"name":"getReceiverPresentationStatus","outputs":[{"name":"exists","type":"bool"},{"name":"status","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"subject","type":"address"}],"name":"getSubjectPresentationList","outputs":[{"name":"","type":"uint256"},{"name":"","type":"bytes32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"subjectPresentationListRegistry","outputs":[{"name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"subjectPresentationHash","type":"bytes32"},{"name":"status","type":"uint8"}],"name":"updateSubjectPresentation","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_previousPublishedVersion","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"name":"hash","type":"bytes32"},{"indexed":False,"name":"status","type":"uint8"}],"name":"PresentationUpdated","type":"event"}]
        )
