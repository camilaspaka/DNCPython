from faker import Faker

# Cria uma instância do Faker
fake = Faker('pt_BR')  # Use 'pt_BR' para dados em português brasileiro

# Gera dados para 10 pessoas
for _ in range(10):
    nome = fake.name()
    cpf = fake.cpf()
    telefone = fake.phone_number()
    email = fake.email()
    endereco = fake.address()

    # Exibe os dados lado a lado
    print(f"Nome: {nome}\nCPF: {cpf}\nTelefone: {telefone}\nEmail: {email}\nEndereço: {endereco}\n{'='*30}\n")
