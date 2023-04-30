def soma(*nums):
    """
    Exemplo de função com parâmetros arbitrários
    """
    print(type(nums))
    soma = 0
    for num in nums:
        soma += num
    return soma
