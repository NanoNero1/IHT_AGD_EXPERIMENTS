# NOTE: I think it might be useful to keep the setups here, at least for now since we change the settings often
setup_ihtAGD = {
    "scheme":"ihtAGD" ,
    "sparsity":0.90,
    "kappa":5.0,
    "beta":50.0}

setup_vanillaAGD = {
    "scheme":"vanillaAGD",
    "kappa":5.0,
    "beta":50.0,
    }

setup_ihtSGD = {
    "scheme":"ihtSGD" ,
    "sparsity":0.900,
    "beta": 50.0,}

setup_vanillaSGD = {
    "scheme":"vanillaSGD",
    "sparsity":0.9,
    "beta": 50.0,
}

setup_pytorchSGD = {
    "scheme":"pytorchSGD"
}

setup_ihtAGD = {
    "scheme":"ihtAGD" ,
    "sparsity":0.90,
    "kappa":5.0,
    "beta":50.0}

setups = [setup_vanillaAGD,setup_ihtAGD,setup_vanillaSGD,setup_ihtSGD]