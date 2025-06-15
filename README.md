# Personal Finances

A Django web application for personal finance management that helps users track their expenses, income, and manage multiple wallets in different currencies.

## Features

- 🔐 User authentication and registration
- 💰 Multi-currency wallet management
- 📊 Transaction tracking (Income/Expense/Transfer)
- 📈 Basic dashboard with transaction history
- 💱 Currency conversion support

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (development)
- **Authentication:** Django's built-in auth system

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/personal-finances.git
cd personal-finances
```

2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python backend/manage.py migrate
```

5. Start the development server
```bash
python backend/manage.py runserver
```

## Project Structure

```
personal-finances/
├── backend/
│   ├── users/          # User management app
│   ├── wallets/        # Wallet and transaction management
│   └── transactions/   # Transaction handling
└── requirements.txt    # Project dependencies
```

## Contributing

This project is currently in development. Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

💡 Idea: Dashboard de Finanzas Personales Colaborativo
🧩 Descripción
Una app donde los usuarios pueden:

Registrar ingresos y gastos.

Ver estadísticas en un dashboard interactivo.

Compartir carteras con otros usuarios (modo colaborativo, por ejemplo, para parejas o compañeros de piso).

Tener control de permisos (solo lectura, lectura/escritura).

Usar tags/categorías y filtros.

🛠️ Tecnologías
🔙 Backend: Django + Django REST Framework
API REST para operaciones CRUD de movimientos financieros.

Autenticación con JWT o tokens.

Permisos por usuario y por cartera.

Uso de PostgreSQL como base de datos.

Tests con pytest o unittest.

🔝 Frontend: React con TypeScript
Framework moderno, muy demandado.

Usa Redux o React Query para manejar el estado.

Gráficas interactivas con Recharts o Chart.js.

Interfaz pulida con Tailwind CSS o MUI.

🐳 Docker
Contenedores separados para:

Django API.

React frontend.

Base de datos PostgreSQL.

Opcional: Nginx como reverse proxy.

Docker Compose para orquestar.

⚙️ Funcionalidades mínimas
Registro e inicio de sesión.

Creación de carteras (una por defecto al crear cuenta).

Añadir transacciones (ingresos/gastos).

Dashboard con gráficas filtrables.

Invitar a otro usuario a tu cartera (colaboración).

Ver historial de movimientos.

🧪 Bonus/Extensiones
Exportar datos a CSV/Excel.

Notificaciones por email (por ejemplo, límite mensual alcanzado).

Tema claro/oscuro.

Deploy en un VPS o con Docker en Railway/Render.




## Database design

table Users
    username uuid PK
    name varchar
    password varchar
    created_at datetime


table Transactions
    id uuid PK
    



