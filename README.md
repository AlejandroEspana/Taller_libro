# Taller Django Libros

Aplicacion Django para administrar autores y libros con CRUD completo.

## Ejecutar localmente

```powershell
venv\Scripts\activate
python manage.py migrate
python manage.py runserver
```

Abrir:

```text
http://127.0.0.1:8000/
```

## Probar

```powershell
python manage.py check
python manage.py test
```

## Desplegar en Vercel

Vercel detecta proyectos Django por `manage.py` y puede ejecutar la app por WSGI. El proyecto incluye:

- `requirements.txt` con dependencias.
- `pyproject.toml` con version de Python y script de build.
- `wsgi.py` en la raiz exponiendo `app`.
- Configuracion para `.vercel.app` en `ALLOWED_HOSTS`.
- Soporte para `DATABASE_URL` usando Postgres.

Variables de entorno recomendadas en Vercel:

```text
DJANGO_SECRET_KEY=<clave-segura>
DATABASE_URL=<url-de-postgres>
```

Despues de configurar `DATABASE_URL`, haz un redeploy. El build ejecuta:

```powershell
python manage.py migrate
python manage.py collectstatic --noinput
```

Si necesitas aplicar migraciones manualmente a Railway desde tu equipo, configura temporalmente `DATABASE_URL` con la URL publica de Railway y ejecuta:

```powershell
$env:DATABASE_URL="postgresql://usuario:password@host-publico:puerto/base"
python manage.py migrate
Remove-Item Env:\DATABASE_URL
```

Para generar una clave local:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Importante: SQLite sirve para probar localmente. En Vercel, usa una base de datos Postgres para que crear, editar y eliminar datos persista correctamente.
