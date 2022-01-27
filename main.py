from ast import Add
from owlready2 import *

crypto = owlready2.get_ontology("crypto_ontology.owl")


with crypto:
    # Classes
    class Blockchain(Thing):
        pass

    # Properties of Blockchain
    class is_proof_of_work(DataProperty, FunctionalProperty):
        domain = [Blockchain]
        range = [bool]

    class is_proof_of_stake(DataProperty, FunctionalProperty):
        domain = [Blockchain]
        range = [bool]

    class is_eco_friendly(DataProperty, FunctionalProperty):
        domain = [Blockchain]
        range = [bool]
        equivalent_to = [Blockchain & Not(is_proof_of_work) & is_proof_of_stake]

    # The main blockchains
    class Ethereum(Blockchain):
        is_proof_of_work = True

    class Ethereum2(Blockchain):
        is_proof_of_work = False

    class Bitcoin(Blockchain):
        is_proof_of_work = True

    class Doge(Blockchain):
        is_proof_of_work = True

    class Cardano(Blockchain):
        is_proof_of_stake = True

    # Other

    class Asset(Thing):
        pass

    class Address(Thing):
        pass

    class ContractAddress(Address):
        pass

    class is_on_blockchain(ObjectProperty): 
        domain = [Address]
        range = [Blockchain]
        
    class ERC20(ContractAddress):
        is_on_blockchain = [Ethereum, Ethereum2]


    class ERC721(ContractAddress):
        is_on_blockchain = [Ethereum, Ethereum2]

    class Reward(Thing):
        pass

    class Exchange(Thing):
        pass

    class CentralizedExchange(Exchange):
        pass

    class DecentralizedExchange(Exchange):
        pass



# Blockchains
ethereum = Ethereum()
ethereum2 = Ethereum2()
bitcoin = Bitcoin()
cardano = Cardano()

# Exchanges
binance = CentralizedExchange("Binance")
bitfinex = CentralizedExchange("Bitfinex")
kraken = CentralizedExchange("Kraken")
uniswap = DecentralizedExchange("Uniswap")
dydx = DecentralizedExchange("DyDx")
pankake_swap = DecentralizedExchange("PankakeSwap")


print(list(crypto.classes()))
