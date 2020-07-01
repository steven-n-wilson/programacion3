# Love My Robot
Este repositorio contiene todo lo necesario para que usted inicie el desarrollo del proyecto.

Note como cada proyecto vive asiladamente dentro de su propio folder.


Use este README para llenarlo con su informacion:

- Usage:
  - RUN python file named lex
  - Open http://127.0.0.1:8085/ in Microsoft Edge browser
  - Open bash terminal
  - Navigate to gui folder
  - RUN node server.js
  - Open http://127.0.0.1:8080/
  - Connect Cozmo
  - Add program instructions in http://127.0.0.1:8080/
- Alguna explicacion extra.


# Compilar / Build

docker-compose build --parallel


# Correr y compilar antes

docker-compose up --build



# Correr

docker-compose up

docker-compose down -v

# Probar solo un app y compilar antes

docker-compose up --build lex
