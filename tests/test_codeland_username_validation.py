from src.coderbyte.codeland_username_validation import (
    CodelandUsernameValidation,
)


def test_validador_menor_4():
    assert CodelandUsernameValidation('a234').validador() is False


def test_validador_maior_25():
    assert (
        CodelandUsernameValidation('a234567890123456789012345').validador()
        is False
    )


def test_validador_comeca_com_letra():
    assert CodelandUsernameValidation('1aa').validador() is False


def test_validador_termina_com_():
    assert CodelandUsernameValidation('aa_').validador() is False


def test_validador_correto():
    assert CodelandUsernameValidation('u__hello_world123').validador() is True
