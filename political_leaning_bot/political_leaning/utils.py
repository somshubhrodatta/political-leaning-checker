import joblib
import numpy as np

# Load trained model (to be created later)
try:
    model = joblib.load('political_leaning/model.sav')
except FileNotFoundError:
    model = None  # Fallback to rule-based if model not trained

QUESTIONS = [
    {"text": "Government should regulate businesses to protect consumers.", "leaning": "left"},
    {"text": "Elections should be publicly funded to reduce corporate influence.", "leaning": "left"},
    {"text": "Strong military spending is essential for national security.", "leaning": "right"},
    {"text": "Voter ID laws are necessary to prevent election fraud.", "leaning": "right"},
    {"text": "International organizations like the UN should have more authority.", "leaning": "left"},
    {"text": "Universal healthcare is a fundamental right.", "leaning": "left"},
    {"text": "Affirmative action is needed to address historical inequalities.", "leaning": "left"},
    {"text": "Immigration policies should prioritize border security.", "leaning": "right"},
    {"text": "Traditional family values should guide societal norms.", "leaning": "right"},
    {"text": "Public education should include diverse perspectives on history.", "leaning": "left"},
    {"text": "Tax cuts for corporations stimulate economic growth.", "leaning": "right"},
    {"text": "A universal basic income would reduce poverty effectively.", "leaning": "left"},
    {"text": "Free market competition drives innovation better than government intervention.", "leaning": "right"},
    {"text": "Wealth taxes are necessary to reduce income inequality.", "leaning": "left"},
    {"text": "Labor unions are critical for protecting workers’ rights.", "leaning": "left"},
    {"text": "Big tech companies should face stricter regulations.", "leaning": "left"},
    {"text": "AI development should prioritize economic growth over ethical concerns.", "leaning": "right"},
    {"text": "Data privacy laws should limit corporate surveillance.", "leaning": "left"},
    {"text": "Cryptocurrencies should remain unregulated to encourage innovation.", "leaning": "right"},
    {"text": "Climate change requires urgent government-led action.", "leaning": "left"},
]

def predict_leaning(answers):
    if model:
        answers_array = np.array([answers])
        label = model.predict(answers_array)[0]
    else:
        # Fallback rule-based scoring
        score = 0
        for i, question in enumerate(QUESTIONS):
            answer = answers[i]
            if question["leaning"] == "left":
                score += (answer - 3)
            else:
                score += (3 - answer)
        score = max(min(score, 20), -20)  # Adjusted for 20 questions
        label = get_label_from_score(score)
    comparison = get_comparison(label)
    return {'label': label, 'score': score if not model else sum(answers)/20-3, 'comparison': comparison}

def get_label_from_score(score):
    if score <= -14:
        return "Far Left"
    elif score <= -5:
        return "Left"
    elif score <= 4:
        return "Center"
    elif score <= 13:
        return "Right"
    else:
        return "Far Right"

def get_comparison(label):
    comparisons = {
        'Far Left': "Similar to Bernie Sanders or socialist policies.",
        'Left': "Aligns with progressive Democrats or EU social democrats.",
        'Center': "Close to moderates like Joe Biden or centrist think tanks.",
        'Right': "Similar to Republicans or UK Conservatives.",
        'Far Right': "Aligns with libertarians or far-right movements like AfD."
    }
    return comparisons[label]