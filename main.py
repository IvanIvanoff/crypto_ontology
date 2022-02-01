from ast import Add
from calendar import c
from owlready2 import *

onto = owlready2.get_ontology("crypto_ontology.owl")


with onto:
    # sync_reasoner()

    # Basic classes that are used as building blocks

    class Blockchain(Thing):
        # A blockchain is the distributed ledger that records and confirms
        # transactions between addresses.
        pass

    class EnvironmentFriendlyBlockchain(Blockchain):
        # A blockchain is environment friendly if the cryptography proof
        # conesus mechanism it uses is not based on work that spends a lot
        # of computation resources to work.
        is_cryptography_proof_energy_efficient = True
    
    class BlockchainName(owlready2.DataProperty, owlready2.FunctionalProperty):
        domain = [Blockchain]
        range = [str]

    class Address(Thing):
        # A blockchain address is simular to a bank account. To control
        # an address one must have its private key
        pass

    class ContractAddress(Address):
        # A contract address is an address where a smart contract is deployed.
        # The smart contract can conform to different token standards. In the
        # scope of this ontology, contract addresses will be used only on the
        # Ethereum blockchains (1 & 2)
        pass

    class TokenStandard(Thing):
        # A token standard is a template of functions and behaviours that a 
        # contract must implement.
        pass

    class ERC20TokenStandard(TokenStandard):
        # The ERC20 token standard that requires the contract to implement the following
        # functions: totalSupply, balanceOf transfer, transferFrom, approve, allowance
        # Every token issued is fungible just like fiat money where 1 lev is the same
        # as any other 1 lev
        pass
    
    class ERC721TokenStandard(TokenStandard):
        # The ERC721 standard represents ownership of a non-fungible token. 
        # A non-fungible token is a token, that is unique in the world, unlike 
        # fiat money in the real world where 1 lev is the same as any other 1 lev.
        pass

    class ERC1155TokenStandard(TokenStandard):
        # The ERC1155 improves upon ERC721 in several key points. It can be
        # used to issue both fungible and non-fungible tokens, but in the real
        # world it is used more for non-fungible tokens. ERC20 is still the dominant
        # fungible tokens standard.
        pass
    
    
    class Token(Thing):
        pass
    
    # Properties of Blockchain
    class CryptographyProof(Thing):
        # The cryptography proof is the method used by the blockchain to verify
        # transactions. This includes method that are based on hard-to-compute
        # math problems or use other methods that are not computational intensive.
        pass

    class ProofOfWork(CryptographyProof):
        # Proof of work works by searching for a random prefix to a given binary,
        # that when it's hashed, the resulting hash starts with a specific number
        # of leading zeros.
        pass

    class ProofOfStake(CryptographyProof):
        # Proof of stake, unlike proof of work where you verify blocks based on your
        # computational power, uses your stash of cryptocurrencies to verify blocks.
        # The algorithm prevents users from lying by "slashing" - if you lie in your
        # verification your cryptocurrencies get deleted, so you lose money.
        pass

    class has_cryptography_proof(Blockchain >> CryptographyProof):
        pass

    class is_cryptography_proof_energy_efficient(Blockchain >> bool):
        pass

    class cryptography_proof_used_by(CryptographyProof >> Blockchain):
        inverse_propery = has_cryptography_proof

    class has_token_standard(Blockchain >> TokenStandard):
        pass

    class token_standard_belongs_to(TokenStandard >> Blockchain):
        inverse_propery = has_token_standard
        
    class has_blockchain_name(Blockchain >> BlockchainName):
        pass

    class is_turing_complete(Blockchain >> bool):
        pass

    class has_non_fungible_tokens(Blockchain >> bool):
        pass

    class is_environment_friendly(DataProperty, FunctionalProperty):
        domain = [Blockchain]
        range = [bool]
        equivalent_to = [
            Blockchain & 
            is_cryptography_proof_energy_efficient.some(True)
        ]

    # The main blockchains

    class Ethereum(Blockchain):
        equivalent_to = [
            Blockchain &
            has_cryptography_proof.some(ProofOfWork) &
            is_turing_complete.some(True) &
            has_blockchain_name.only("Ethereum")
        ]

    class Ethereum2(Blockchain):
       equivalent_to = [
            Blockchain &
            has_cryptography_proof.some(ProofOfStake) &
            is_turing_complete.some(True) &
            has_blockchain_name.only("Ethereum2")
        ]

    class Bitcoin(Blockchain):
         equivalent_to = [
            Blockchain &
            has_cryptography_proof.some(ProofOfWork) &
            is_turing_complete.some(False) &
            has_blockchain_name.only("Bitcoin")
        ]

    class Cardano(Blockchain):
        equivalent_to = [
            Blockchain &
            has_cryptography_proof.some(ProofOfStake) &
            is_turing_complete.some(True) &
            has_blockchain_name.only("Cardano")
        ]

    class MarketSegment(Thing):
        pass
    
    class is_on_blockchain(Address >> Blockchain):
        pass

    # Other
        
    class ERC20ContractAddress(ContractAddress):
        equivalent_to = [
            Address & 
            (is_on_blockchain.some(Ethereum) | is_on_blockchain.some(Ethereum2)) &
            has_token_standard.some(ERC20TokenStandard)
        ]
     
    class ERC721ContractAddress(ContractAddress):
        equivalent_to = [
            Address & 
            (is_on_blockchain.some(Ethereum) | is_on_blockchain.some(Ethereum2)) &
            has_token_standard.some(ERC721TokenStandard)
        ]


    class ERC1155ContractAddress(ContractAddress):
        equivalent_to = [
            Address & 
            (is_on_blockchain.some(Ethereum) | is_on_blockchain.some(Ethereum2)) &
            has_token_standard.some(ERC721TokenStandard)
        ]

    # Exchanges

    class Exchange(Thing):
        pass

    class CentralizedExchange(Exchange):
        pass

    class DecentralizedExchange(Exchange):
        pass

close_world(onto)

# Blockchains
ethereum = Ethereum()
ethereum2 = Ethereum2()
bitcoin = Bitcoin()
doge = Doge()
cardano = Cardano()

# AllDifferent([ethereum, ethereum2, bitcoin, doge, cardano])

# Exchanges
binance = CentralizedExchange("Binance")
bitfinex = CentralizedExchange("Bitfinex")
kraken = CentralizedExchange("Kraken")
uniswap = DecentralizedExchange("Uniswap")
dydx = DecentralizedExchange("DyDx")
pankake_swap = DecentralizedExchange("PankakeSwap")

# AllDifferent([ binance, bitfinex, kraken, uniswap, dydx, pankake_swap ])


print(ethereum2.is_environment_friendly)

