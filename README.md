# massasmias-backend

## Requisitos

### Requisitos Funcionais

1. **Cadastro de Usuários** 
- Qualquer usuário deve ter acesso ao formulário de cadastro com campos obrigatórios para nome, e-mail, telefone, data de nascimento, endereço (rua, número, bairro) e senha.
- O site deve se ter validação de e-mail e telefone (ex.: formato correto, e-mail único).

2. **Login de Usuários**
- O site deve conter um formulário de login com campos para e-mail ou telefone e senha para qualquer usuário.

3. **Recuperação de Senha**
- O site deve conter um formulário de recuperação de senha com os campos nome e email.

4. **Cardápio Online**
- O site deve exibir itens do menu (cardápio), divididos em categorias (entradas, pratos principais, sobremesas, bebidas).
- O menu (cardápio) deve conter descrições detalhadas de cada item, incluindo preços e fotos.
- O site deve possuir um campo para especificação de preferências alimentares e restrições na reserva (checkbox, para seleção, por exemplo).

5. **Reserva de Mesas**
- O site deve apresentar um formulário para reservas (mapa de mesas), com campos para nome, número de pessoas, data e hora.

6. **Pedidos Online** 
- O site deve permitir que clientes façam pedidos online para entrega ou retirada.
- A opção de acompanhar o status do pedido deve aparecer.

7. **Sistema de Avaliações**
- O site deve permitir que clientes deixem avaliações e notas.
- O site deve exibir avaliações e comentários de clientes anteriores.

8. **Requisitos para Administradores**
- Os admins devem conseguir gerenciar seus usuários (possibilitando visualizar, editar e deletar usuários).
- Os admins devem conseguir gerenciar os itens do menu (cardápio) (possibilitando visualizar, adicionar, editar e deletar os itens do menu)
- Os admins devem conseguir gerenciar as reservas (possibilitando visualizar, adicionar, editar e cancelar(deletar) as reservas)
- Os admins devem conseguir gerenciar os pedidos dos usuários 
- Os admins devem conseguir gerenciar as avaliações (possibilitando visualizar e deletar avaliações)
    
### Requisitos Não Funcionais

1. **Acessibilidade** 
- Garantir que o site seja acessível para pessoas com deficiências visuais/ auditivas

2. **Segurança**
- Hashing seguro das senhas no banco de dados
- O site deve conter diferentes níveis de acesso (usuarios comuns e administradores)

3. **Usabilidade**
- O site deve conter a interface de usuário intuitiva e fácil de usar.
- O design do site deve ser responsivo para funcionar bem em dispositivos móveis e desktops.
- O site deve conter um painel administrativo fácil de usar e navegar.

# massasmias-frontend

## Requisitos Funcionais

1. **Interface de Usuário Responsiva**
- o design do site deve ser responsivo, que se adapta a diferentes tamanhos de tela (desktop, tablet, mobile).
- o layout do site deve ser consistente e intuitivo em todas as páginas.

2. **Navegação**
- A navegação do site deve ser clara (intuitiva) e acessível em todas as páginas.

3. **Componentes Visuais**
- o site deve fazer listagens dos itens do menu com imagens, descrições e preços.
- O site deve conter formulários para reservas, pedidos.

4. **Interatividade**
- Formulário para os usuários deixarem avaliações e comentários.
- Exibição de avaliações e comentários na página do restaurante.

5. **Interface Administrativa**
- o site deve conter um painel de controle (dashboard) com estatísticas e resumos (ex.: usuários, pedidos, avaliações, itens do menu).

### Requisitos Não Funcionais

1. **Acessibilidade** 
- É essêncial garantir que o site seja acessível para pessoas com deficiências visuais.

2. **Segurança**
- O site deve possuir hashing seguro das senhas no banco de dado.

3. **Usabilidade**
- A interface de usuário deve ser intuitiva e fácil de usar
- O design deve ser responsivo para funcionar bem em dispositivos móveis e desktops.


# massasmias-mobile

## Requisitos Funcionais

1. **Aplicativo Nativo**
- Aplicativo disponível para Android
- Interface amigável e adaptada para dispositivos móveis.

2. **Autenticação e Perfis de Usuários**
- Cadastro, login, e recuperação de senha.

3. **Menu e Pedidos Online**
- Visualização do menu com imagens e descrições.

4. **Reservas**
- Mapa de mesas com reservas disponíveis.

5. **Sistema de Avaliações**
- Avaliação de pratos e serviços.
- Visualização de avaliações de outros clientes.

## Requisitos Não Funcionais

1. **Desempenho**
- Aplicativo rápido e responsivo.

2. **Usabilidade**
- Interface de usuário intuitiva e fácil de navegar.

3. **Segurança**
- Criptografia de dados (senha).

4. **Acessibilidade**
- Conformidade com as diretrizes de acessibilidade móvel.

## Tarefas 

1. **Usuários**
- [] Criar modelo de dados para usuários/admins, itens do cardápio, reservas, pedidos e avaliações no banco de dados.
- [] Implementar endpoint para cadastro de usuários.
- [] Validar e-mail e telefone no backend (formato correto, email único).
- [] Implementar endpoint de login de usuários.
- [] Criar endpoint para solicitação de recuperação de senha.
- [] Implementar endpoints para gerenciamento de usuários (visualizar, editar, deletar).
- [] Implementar endpoints para gerenciamento de itens do cardápio (visualizar, adicionar, editar, deletar).
- [] Implementar endpoints para gerenciamento de reservas (visualizar, adicionar, editar, cancelar(deletar)).
- [] Implementar endpoints para gerenciamento de pedidos (visualizar, atualizar status, concluir(deletar)).
- [] Implementar endpoints para gerenciamento de avaliações (visualizar, deletar).

2. **Menu (Cardápios)**
- [] Criar modelo de dados para itens do cardápio.
- [] Desenvolver lógica para exibição de itens divididos por categorias.
- [] Implementar campo para especificação de preferências alimentares e restrições.

3. **Reservas de mesas**
- [] Criar modelo de dados para reservas de mesas.
- [] Implementar endpoint para criar reservas.
- [] Desenvolver endpoint para editar e cancelar reservas.
- [] Implementar lógica para exibição de mapa de mesas disponíveis.

4. **Pedidos**
- [] Criar modelo de dados para pedidos.
- [] Implementar endpoints para criar, atualizar e cancelar (deletar) pedidos.
- [] Desenvolver lógica para acompanhamento do status do pedido.

5. **Avaliações dos Usuários**
- [] Criar modelo de dados para avaliações.
- [] Implementar endpoints para criar, moderar e exibir avaliações.
- [] Desenvolver lógica para moderação e exibição de avaliações.