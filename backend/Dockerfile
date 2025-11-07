# Etapa 1: imagem com Java e Gradle para compilar o projeto
FROM gradle:8.7.0-jdk21 AS builder
WORKDIR /app
COPY . .
RUN gradle clean bootJar --no-daemon

# Etapa 2: imagem leve apenas para rodar o aplicativo
FROM eclipse-temurin:21-jdk
WORKDIR /app

# Copia o JAR gerado na etapa anterior
COPY --from=builder /app/build/libs/*.jar app.jar

# Garante que arquivos estáticos (HTML, CSS, JS) sejam incluídos no jar
COPY src/main/resources/static /app/static

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
