# decrypt_rsa

Projeto criado para validar a utilização do python como linguagem para descriptografar payloads criptografados do lado do cliente

Para rodar

1 - Instale as libs necessárias

2 - Rode o comando para gerar a chave privada
```bash
python generate_new_private_key.py 
```
3 - Copie e cole a chave na variável `key` no arquivo `domain/RSA.py`

4 - Utilize o seguinte comando para rodar a aplicação
```bash
uvicorn main:app --reload
```

Utilize o endereço `http://127.0.0.1:8000/docs` para visualizar a documentação dos endpoints

O endpoint `/rsa/get_public_key` é reponsável por retornar a chave publica, essa chave será utilizada pelo front para criptografar

Para testar o fluxo como um todo, gere uma chave publica pelo endpoint e cole nesse simulador aqui, no campo `Public Key`: https://codepen.io/ryantriangles/pen/RyPgEW

Crie um payload no campo `Text to encrypt` e clique para criptografar.

Copie o dado criptografado e utilize o enpoint `/rsa/send_data` para descriptografar. Esse endpoint irá retornar o payload descriptigrafado

