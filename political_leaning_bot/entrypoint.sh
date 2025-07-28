#!/bin/bash
# Check if model.sav exists to avoid retraining on every restart
if [ ! -f political_leaning/model.sav ]; then
    echo "Training model..."
    python train_model.py
else
    echo "Model already trained, skipping training."
fi

# Run Django migrations
python manage.py makemigrations
python manage.py migrate

# Start the Django server
exec gunicorn --bind 0.0.0.0:8000 political_leaning_bot.wsgi