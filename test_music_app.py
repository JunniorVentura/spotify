from music_app import MusicApp, Song

# Función auxiliar para simular la existencia de usuarios
def user_exists(app, username):
    return username in app.users

# Función auxiliar para simular la comprobación de la contraseña correcta
def correct_password(app, username, password):
    return app.users[username].password == password

# 1. Prueba de Partición de Equivalencia
def test_equivalence_partition():
    app = MusicApp()
    app.register_user("user1", "password1")

    # Particiones de Equivalencia
    equivalence_classes = [
        # PE1: Username existe y contraseña es correcta
        ("user1", "password1", "Login successful"),
        # PE2: Username existe y contraseña es incorrecta
        ("user1", "wrongpassword", "Incorrect password"),
        # PE3: Username no existe y contraseña es irrelevante
        ("nonexistentuser", "password1", "Username does not exist"),
        ("nonexistentuser", "wrongpassword", "Username does not exist")
    ]

    for username, password, expected in equivalence_classes:
        result = app.login_user(username, password)
        assert result == expected, f"Expected result: {expected}, but got: {result}"
        print(f"Partición de Equivalencia - Test with {username} and {password} passed.")

# 2. Prueba de Análisis de Valores Frontera
def test_boundary_value_analysis():
    app = MusicApp()
    boundary_tests = [
        # Límite inferior y justo por encima del límite inferior para username
        ("u", "password", "User registered successfully"),       # 1 carácter
        ("us", "password", "User registered successfully"),      # 2 caracteres
        # Límite superior y justo por debajo del límite superior para username
        ("u" * 20, "password", "User registered successfully"),  # 20 caracteres
        ("u" * 19, "password", "User registered successfully"),  # 19 caracteres

        # Límite inferior y justo por encima del límite inferior para password
        ("user", "p", "User registered successfully"),           # 1 carácter
        ("user", "pa", "User registered successfully"),          # 2 caracteres
        # Límite superior y justo por debajo del límite superior para password
        ("user", "p" * 20, "User registered successfully"),      # 20 caracteres
        ("user", "p" * 19, "User registered successfully"),      # 19 caracteres
    ]

    for username, password, expected in boundary_tests:
        result = app.register_user(username, password)
        assert result == expected, f"Expected result: {expected}, but got: {result}"
        print(f"Análisis de Valores Frontera - Test with username: '{username}' and password: '{password}' passed.")

# 3. Prueba de Tabla de Decisión
def test_decision_table():
    app = MusicApp()
    app.register_user("user1", "password1")

    decision_table = [
        ("user1", "password1", "Login successful"),   # Correct user and password
        ("user1", "wrongpassword", "Incorrect password"), # Correct user, wrong password
        ("wronguser", "password1", "Username does not exist"), # Wrong user, correct password
        ("wronguser", "wrongpassword", "Username does not exist"), # Wrong user, wrong password
    ]

    for username, password, expected in decision_table:
        result = app.login_user(username, password)
        assert result == expected, f"Expected result: {expected}, but got: {result}"
        print(f"Tabla de Decisión - Test with {username} and {password} passed.")

# 4. Prueba de Transición de Estado
def test_state_transition():
    app = MusicApp()
    app.register_user("user1", "password1")

    # Caso 1: Credenciales correctas en el primer intento
    result = app.login_user("user1", "password1")
    assert result == "Login successful", f"Expected 'Login successful', but got '{result}'"
    print("Transición de Estado - Test 1 passed.")

    # Caso 2: Credenciales incorrectas tres veces seguidas
    app.login_user("user1", "wrongpassword")  # Intento 1 fallido
    app.login_user("user1", "wrongpassword")  # Intento 2 fallido
    result = app.login_user("user1", "wrongpassword")  # Intento 3 fallido
    assert result == "User locked", f"Expected 'User locked', but got '{result}'"
    print("Transición de Estado - Test 2 passed.")

    # Caso 3: Credenciales correctas después de tres intentos fallidos
    result = app.login_user("user1", "password1")
    assert result == "User locked", f"Expected 'User locked', but got '{result}'"
    print("Transición de Estado - Test 3 passed.")

# Run tests
if __name__ == "__main__":
    test_equivalence_partition()
    test_boundary_value_analysis()
    test_decision_table()
    test_state_transition()
