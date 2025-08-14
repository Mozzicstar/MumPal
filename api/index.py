from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from datetime import date, datetime, timedelta
import random

app = Flask(__name__)
app.secret_key = 'helpmumpal_secret_key_2025'

# Initialize session data
def init_session():
    if 'user_data' not in session:
        session['user_data'] = {
            'pregnancy_week': 28,
            'baby_age_months': 3,
            'reminders': [],
            'health_logs': [],
            'chat_history': [],
            'journal_entries': [],
            'emergency_contacts': ['112', 'Mama'
            'Care Center, Ibadan']
        }

@app.route('/')
def home():
    init_session()
    return render_template('home.html')

@app.route('/ai_assistant')
def ai_assistant():
    init_session()
    return render_template('ai_assistant.html', chat_history=session['user_data'].get('chat_history', []))

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    init_session()
    question = request.form.get('question')
    
    if question:
        # AI responses with comprehensive health guidance
        ai_responses = {
            'morning sickness': "Morning sickness is common in early pregnancy, affecting up to 80% of pregnant women. Try eating small, frequent meals throughout the day, avoid spicy or fatty foods, and consider ginger tea or ginger supplements. Stay hydrated and eat bland foods like crackers or toast. If you're unable to keep food or fluids down for more than 24 hours, contact your healthcare provider immediately as this could indicate hyperemesis gravidarum.",
            
            'baby feeding': "For newborns, breastfeeding is recommended exclusively for the first 6 months. Newborns typically feed 8-12 times per day, about every 2-3 hours. Signs your baby is getting enough milk include steady weight gain, regular wet diapers (6+ per day), and contentment between feeds. If breastfeeding isn't possible, formula feeding every 3-4 hours works well. Always ensure proper latch and seek support from a lactation consultant if needed.",
            
            'postpartum depression': "Postpartum depression affects 10-20% of new mothers and is a serious but treatable condition. Symptoms include persistent sadness, anxiety, difficulty bonding with your baby, changes in appetite or sleep patterns, and thoughts of self-harm. This is different from 'baby blues' which typically resolve within 2 weeks. Professional help is available and very effective - including therapy, support groups, and sometimes medication that's safe while breastfeeding. You are not alone, and seeking help shows strength.",
            
            'weight gain': "Healthy weight gain during pregnancy depends on your pre-pregnancy BMI. Generally: underweight women should gain 28-40 lbs, normal weight 25-35 lbs, overweight 15-25 lbs, and obese 11-20 lbs. Focus on nutritious foods including fruits, vegetables, whole grains, lean proteins, and dairy. Avoid empty calories from sugary drinks and processed foods. Regular, moderate exercise as approved by your doctor is beneficial. Sudden weight gain or loss should be discussed with your healthcare provider.",
            
            'sleep': "Sleep disruption is very common with newborns who don't yet have established circadian rhythms. Try to rest whenever your baby sleeps, even during the day. Share night feeding duties with your partner if possible. Create a calm bedtime routine for yourself and baby. Keep baby's nighttime environment dim and quiet. Consider safe co-sleeping options like bedside bassinets. If severe sleep deprivation affects your daily functioning or mood, discuss with your healthcare provider.",
            
            'contractions': "True labor contractions are regular, progressively stronger, and don't stop with movement or position changes. They typically start 20+ minutes apart and gradually get closer together. Braxton Hicks (practice contractions) are irregular and often stop with movement. Call your healthcare provider when contractions are 5 minutes apart, lasting 60 seconds, for at least 1 hour (5-1-1 rule). Also call immediately if you experience water breaking, heavy bleeding, or decreased fetal movement.",
            
            'breastfeeding problems': "Common breastfeeding challenges include sore nipples, engorgement, low milk supply, and difficulty with latch. For sore nipples, ensure proper latch and try different positions. For engorgement, feed frequently and use warm compresses before feeding, cold after. To increase milk supply, feed more frequently, stay hydrated, get adequate rest, and consider pumping after feeds. If problems persist, contact a lactation consultant or your healthcare provider.",
            
            'baby development': "Every baby develops at their own pace, but general milestones include: 2 months - smiling, following objects; 4 months - holding head steady, laughing; 6 months - sitting with support, babbling; 9 months - crawling, saying 'mama/dada'; 12 months - walking, first words. Red flags include not making eye contact by 2 months, not smiling by 3 months, or significant loss of previously acquired skills. Regular pediatric checkups monitor development appropriately.",
            
            'nutrition pregnancy': "During pregnancy, focus on nutrient-dense foods: folate (leafy greens, citrus, fortified grains), iron (lean meats, beans, spinach), calcium (dairy, fortified plant milks), omega-3 fatty acids (fish, walnuts, flax seeds), and protein (lean meats, eggs, legumes). Take prenatal vitamins as recommended. Avoid alcohol, limit caffeine to 200mg daily, avoid high-mercury fish, and ensure meats are fully cooked. Stay hydrated with 8-10 glasses of water daily.",
            
            'mental health': "Mental health during pregnancy and postpartum is just as important as physical health. It's normal to experience mood changes, but persistent symptoms lasting more than 2 weeks warrant professional attention. These include: persistent sadness, anxiety, irritability, difficulty concentrating, changes in appetite or sleep, or thoughts of self-harm. Treatment options include therapy, support groups, and sometimes medication safe during pregnancy/breastfeeding. Don't hesitate to reach out for help."
        }
        
        # Enhanced keyword matching for more relevant responses
        response = "I understand your concern about your health. Based on current maternal health guidelines, it's important to monitor your symptoms and maintain regular communication with your healthcare provider. Stay hydrated, get adequate rest, maintain a nutritious diet, and don't hesitate to seek immediate medical attention if you experience severe symptoms like heavy bleeding, severe headaches, difficulty breathing, or persistent vomiting. Your health and your baby's health are our top priority."
        
        question_lower = question.lower()
        for keyword, specific_response in ai_responses.items():
            if any(term in question_lower for term in keyword.split()):
                response = specific_response
                break
        
        # Add contextual health warnings
        warning_keywords = ['bleeding', 'pain', 'fever', 'headache', 'vision', 'breathing']
        if any(keyword in question_lower for keyword in warning_keywords):
            response += "\n\n⚠️ **Important:** If you're experiencing severe symptoms, please contact your healthcare provider immediately or call emergency services if needed."
        
        # Add to chat history
        if 'chat_history' not in session['user_data']:
            session['user_data']['chat_history'] = []
        
        session['user_data']['chat_history'].append({
            'question': question,
            'answer': response,
            'timestamp': datetime.now().isoformat()
        })
        
        session.modified = True
    
    return redirect(url_for('ai_assistant'))

@app.route('/baby_tracker')
def baby_tracker():
    init_session()
    return render_template('baby_tracker.html', user_data=session['user_data'])

@app.route('/nutrition_guide')
def nutrition_guide():
    init_session()
    return render_template('nutrition_guide.html')

@app.route('/health_tracker')
def health_tracker():
    init_session()
    return render_template('health_tracker.html', health_logs=session['user_data'].get('health_logs', []))

@app.route('/log_health', methods=['POST'])
def log_health():
    init_session()
    
    new_log = {
        'date': date.today().isoformat(),
        'time': datetime.now().time().strftime('%H:%M'),
        'temperature': float(request.form.get('temperature', 37.0)),
        'weight': float(request.form.get('weight', 65.0)),
        'blood_pressure': f"{request.form.get('blood_pressure_sys')}/{request.form.get('blood_pressure_dia')}",
        'heart_rate': int(request.form.get('heart_rate', 72)),
        'mood': request.form.get('mood'),
        'energy_level': int(request.form.get('energy_level', 5)),
        'sleep_hours': float(request.form.get('sleep_hours', 8.0)),
        'water_intake': int(request.form.get('water_intake', 8)),
        'notes': request.form.get('notes', '')
    }
    
    if 'health_logs' not in session['user_data']:
        session['user_data']['health_logs'] = []
    
    session['user_data']['health_logs'].append(new_log)
    session.modified = True
    
    return redirect(url_for('health_tracker'))

@app.route('/reminders')
def reminders():
    init_session()
    return render_template('reminders.html', reminders=session['user_data'].get('reminders', []))

@app.route('/add_reminder', methods=['POST'])
def add_reminder():
    init_session()
    
    new_reminder = {
        'id': len(session['user_data'].get('reminders', [])) + 1,
        'type': request.form.get('reminder_type'),
        'title': request.form.get('title'),
        'date': request.form.get('reminder_date'),
        'time': request.form.get('reminder_time'),
        'frequency': request.form.get('frequency'),
        'description': request.form.get('description', ''),
        'priority': request.form.get('priority'),
        'status': 'Active',
        'created': datetime.now().isoformat()
    }
    
    if 'reminders' not in session['user_data']:
        session['user_data']['reminders'] = []
    
    session['user_data']['reminders'].append(new_reminder)
    session.modified = True
    
    return redirect(url_for('reminders'))

@app.route('/emergency_help')
def emergency_help():
    init_session()
    return render_template('emergency_help.html')

@app.route('/mental_health')
def mental_health():
    init_session()
    return render_template('mental_health.html', journal_entries=session['user_data'].get('journal_entries', []))

@app.route('/save_journal', methods=['POST'])
def save_journal():
    init_session()
    
    journal_entry = {
        'date': date.today().isoformat(),
        'entry': request.form.get('journal_entry'),
        'mood': request.form.get('mood_check')
    }
    
    if 'journal_entries' not in session['user_data']:
        session['user_data']['journal_entries'] = []
    
    session['user_data']['journal_entries'].append(journal_entry)
    session.modified = True
    
    return redirect(url_for('mental_health'))

@app.route('/get_affirmation')
def get_affirmation():
    affirmations = [
        "You are doing an amazing job, even when it doesn't feel like it",
        "It's okay to ask for help - that shows strength, not weakness", 
        "Your baby is lucky to have you as their mother",
        "Taking care of yourself is taking care of your family",
        "Every mother struggles sometimes - you are not alone",
        "Your feelings are valid and temporary",
        "You are stronger than you know",
        "It's okay to take breaks and rest"
    ]
    
    return jsonify({'affirmation': random.choice(affirmations)})

@app.route('/resources')
def resources():
    init_session()
    return render_template('resources.html')

@app.route('/about')
def about():
    init_session()
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)