import streamlit as st

st.set_page_config(
    page_title="دستیار شرح حال قلب",
    page_icon="❤️",
    layout="wide"
)

# ---------------------------------------------------------
# CSS - Persian RTL GUI
# ---------------------------------------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}

.stTextInput, .stTextArea, .stSelectbox,
.stNumberInput, .stMultiSelect {
    direction: rtl;
    text-align: right;
}

div[data-testid="stRadio"] {
    direction: rtl;
}

button {
    direction: rtl;
}

textarea {
    direction: rtl !important;
    text-align: right !important;
}

input {
    direction: rtl !important;
    text-align: right !important;
}

h1, h2, h3, h4 {
    direction: rtl;
    text-align: right;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

st.title("❤️ دستیار هوشمند شرح حال بیمار قلبی")

st.caption(
    "تکمیل شرح حال اولیه بیمار و تولید پرامپت ساختاریافته برای ChatGPT"
)

st.warning(
    "این برنامه ابزار کمکی برای جمع‌آوری و سازمان‌دهی اطلاعات است "
    "و جایگزین تشخیص و تصمیم‌گیری پزشک نیست."
)


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

def yes_no(label):
    return st.radio(
        label,
        ["خیر", "بله"],
        horizontal=True
    )


def clean(value):
    if value is None:
        return ""
    return str(value).strip()


# ---------------------------------------------------------
# Prompt Generator
# ---------------------------------------------------------

def build_prompt(data):

    prompt = f"""
You are assisting a licensed cardiologist with structured analysis
of a patient's initial clinical history.

IMPORTANT:
- Do not make a definitive diagnosis from history alone.
- Identify possible differential diagnoses.
- Clearly identify red-flag findings.
- Distinguish urgent findings from non-urgent possibilities.
- Explain what additional clinical evaluation may be considered.
- Do not recommend starting, stopping, or changing prescription medications.
- Do not replace professional medical evaluation.

========================================
PATIENT INFORMATION
========================================

Age: {data['age']}
Sex: {data['sex']}
Height: {data['height']} cm
Weight: {data['weight']} kg
Occupation: {data['occupation']}

========================================
CHIEF COMPLAINT
========================================

Main reason for visit:
{data['chief_complaint']}

When symptoms started:
{data['onset']}

Frequency:
{data['frequency']}

========================================
CHEST PAIN / CHEST DISCOMFORT
========================================

Chest pain/discomfort:
{data['chest_pain']}

Location:
{data['pain_location']}

Pain characteristics:
{data['pain_type']}

Pain intensity (0-10):
{data['pain_intensity']}

Duration:
{data['pain_duration']}

Radiation:
{data['radiation']}

Triggered by physical activity:
{data['activity_trigger']}

Relieved by rest:
{data['rest_relief']}

Changes with breathing:
{data['breathing_change']}

Changes with body movement:
{data['movement_change']}

========================================
ASSOCIATED SYMPTOMS
========================================

Shortness of breath:
{data['dyspnea']}

Palpitations:
{data['palpitations']}

Dizziness:
{data['dizziness']}

Fainting / near-fainting:
{data['syncope']}

Sweating:
{data['sweating']}

Nausea / vomiting:
{data['nausea']}

Fatigue / reduced exercise tolerance:
{data['fatigue']}

Leg / ankle swelling:
{data['edema']}

Orthopnea:
{data['orthopnea']}

Paroxysmal nocturnal dyspnea:
{data['pnd']}

========================================
MEDICAL HISTORY
========================================

Hypertension:
{data['hypertension']}

Diabetes:
{data['diabetes']}

High cholesterol:
{data['hyperlipidemia']}

Kidney disease:
{data['kidney_disease']}

Thyroid disease:
{data['thyroid']}

Previous myocardial infarction:
{data['previous_mi']}

Previous stroke:
{data['stroke']}

Known coronary artery disease:
{data['cad']}

Previous angiography or stent:
{data['angiography']}

Previous bypass surgery:
{data['bypass']}

Known arrhythmia:
{data['arrhythmia']}

Known valvular disease:
{data['valvular']}

Congenital heart disease:
{data['congenital']}

Other medical conditions:
{data['other_conditions']}

========================================
FAMILY HISTORY
========================================

Family history of cardiovascular disease:
{data['family_cvd']}

Family history of myocardial infarction:
{data['family_mi']}

Sudden cardiac death in family:
{data['sudden_death']}

Other relevant family history:
{data['family_other']}

========================================
LIFESTYLE
========================================

Smoking:
{data['smoking']}

Cigarettes per day:
{data['cigarettes']}

Years of smoking:
{data['smoking_years']}

Hookah:
{data['hookah']}

Alcohol:
{data['alcohol']}

Exercise:
{data['exercise']}

Diet:
{data['diet']}

Sleep:
{data['sleep']}

========================================
MEDICATIONS
========================================

Current medications:
{data['medications']}

Drug allergies:
{data['allergies']}

Medication adherence:
{data['adherence']}

========================================
AVAILABLE TEST RESULTS
========================================

Blood pressure:
{data['blood_pressure']}

Heart rate:
{data['heart_rate']}

Oxygen saturation:
{data['oxygen']}

ECG:
{data['ecg']}

Echocardiography:
{data['echo']}

Holter:
{data['holter']}

Stress test:
{data['stress_test']}

Coronary CT / angiography:
{data['coronary_imaging']}

Laboratory results:
{data['labs']}

Other reports:
{data['other_tests']}

========================================
PHYSICIAN'S CLINICAL QUESTION
========================================

{data['clinical_question']}

========================================
REQUESTED ANALYSIS
========================================

Analyze the case using the following structure:

1. Concise clinical summary.

2. Important positive findings.

3. Important negative findings.

4. Cardiovascular risk factors.

5. Possible differential diagnoses.

6. Findings supporting each differential diagnosis.

7. Findings arguing against each differential diagnosis.

8. Red-flag findings requiring urgent medical evaluation.

9. Important missing information.

10. Physical examinations that may be considered.

11. Potential investigations:
   - ECG
   - Blood tests
   - Echocardiography
   - Holter monitoring
   - Stress testing
   - Coronary imaging
   - Other appropriate investigations

12. Explain what additional findings could increase or decrease
    clinical concern.

13. Provide a final structured clinical summary for review
    by the cardiologist.

Do not claim diagnostic certainty when the available information
does not support it.
"""

    return prompt.strip()


# =========================================================
# FORM
# =========================================================

with st.form("فرم_شرح_حال_قلب"):

    # -----------------------------------------------------
    # اطلاعات بیمار
    # -----------------------------------------------------

    st.header("۱. اطلاعات اولیه بیمار")

    c1, c2, c3 = st.columns(3)

    with c1:
        age = st.number_input(
            "سن",
            min_value=0,
            max_value=120,
            value=40
        )

    with c2:
        sex = st.selectbox(
            "جنسیت",
            ["مرد", "زن", "سایر / مشخص نشده"]
        )

    with c3:
        occupation = st.text_input(
            "شغل"
        )

    c1, c2 = st.columns(2)

    with c1:
        height = st.number_input(
            "قد (سانتی‌متر)",
            min_value=0.0,
            value=170.0
        )

    with c2:
        weight = st.number_input(
            "وزن (کیلوگرم)",
            min_value=0.0,
            value=70.0
        )

    # -----------------------------------------------------
    # شکایت اصلی
    # -----------------------------------------------------

    st.header("۲. شکایت اصلی بیمار")

    chief_complaint = st.text_area(
        "دلیل اصلی مراجعه بیمار چیست؟",
        height=100
    )

    c1, c2 = st.columns(2)

    with c1:
        onset = st.text_input(
            "علائم از چه زمانی شروع شده‌اند؟"
        )

    with c2:
        frequency = st.text_input(
            "علائم هر چند وقت یک‌بار اتفاق می‌افتند؟"
        )

    # -----------------------------------------------------
    # درد قفسه سینه
    # -----------------------------------------------------

    st.header("۳. درد یا ناراحتی قفسه سینه")

    chest_pain = yes_no(
        "آیا بیمار درد یا ناراحتی قفسه سینه دارد؟"
    )

    c1, c2 = st.columns(2)

    with c1:

        pain_location = st.text_input(
            "محل درد"
        )

        pain_type = st.multiselect(
            "نوع یا ماهیت درد",
            [
                "فشار",
                "سنگینی",
                "فشردگی",
                "سوزش",
                "تیرکشیدن",
                "درد تیز",
                "درد مبهم",
                "سایر"
            ]
        )

        pain_intensity = st.slider(
            "شدت درد از ۰ تا ۱۰",
            0,
            10,
            0
        )

    with c2:

        pain_duration = st.text_input(
            "مدت هر حمله درد"
        )

        radiation = st.text_input(
            "آیا درد به قسمت دیگری انتشار پیدا می‌کند؟"
        )

        activity_trigger = yes_no(
            "آیا درد با فعالیت بدنی ایجاد یا تشدید می‌شود؟"
        )

        rest_relief = yes_no(
            "آیا درد با استراحت بهتر می‌شود؟"
        )

    breathing_change = yes_no(
        "آیا درد با نفس عمیق تغییر می‌کند؟"
    )

    movement_change = yes_no(
        "آیا درد با حرکت بدن تغییر می‌کند؟"
    )

    # -----------------------------------------------------
    # علائم همراه
    # -----------------------------------------------------

    st.header("۴. علائم همراه")

    c1, c2, c3 = st.columns(3)

    with c1:

        dyspnea = yes_no(
            "تنگی نفس؟"
        )

        palpitations = yes_no(
            "تپش قلب؟"
        )

        dizziness = yes_no(
            "سرگیجه؟"
        )

        syncope = yes_no(
            "غش یا نزدیک به غش؟"
        )

    with c2:

        sweating = yes_no(
            "تعریق غیرعادی؟"
        )

        nausea = yes_no(
            "تهوع یا استفراغ؟"
        )

        fatigue = yes_no(
            "خستگی یا کاهش توان فعالیت؟"
        )

        edema = yes_no(
            "تورم پا یا مچ پا؟"
        )

    with c3:

        orthopnea = yes_no(
            "تنگی نفس هنگام دراز کشیدن؟"
        )

        pnd = yes_no(
            "بیدار شدن شبانه به علت تنگی نفس؟"
        )

    # -----------------------------------------------------
    # سابقه پزشکی
    # -----------------------------------------------------

    st.header("۵. سابقه بیماری‌های قبلی")

    c1, c2, c3 = st.columns(3)

    with c1:

        hypertension = yes_no(
            "فشار خون بالا؟"
        )

        diabetes = yes_no(
            "دیابت؟"
        )

        hyperlipidemia = yes_no(
            "چربی خون بالا؟"
        )

        kidney_disease = yes_no(
            "بیماری کلیوی؟"
        )

        thyroid = yes_no(
            "بیماری تیروئید؟"
        )

    with c2:

        previous_mi = yes_no(
            "سابقه سکته قلبی؟"
        )

        stroke = yes_no(
            "سابقه سکته مغزی؟"
        )

        cad = yes_no(
            "سابقه بیماری عروق کرونر؟"
        )

        angiography = yes_no(
            "سابقه آنژیوگرافی یا استنت؟"
        )

        bypass = yes_no(
            "سابقه جراحی بای‌پس قلب؟"
        )

    with c3:

        arrhythmia = yes_no(
            "سابقه آریتمی؟"
        )

        valvular = yes_no(
            "بیماری دریچه‌ای قلب؟"
        )

        congenital = yes_no(
            "بیماری مادرزادی قلب؟"
        )

    other_conditions = st.text_area(
        "سایر بیماری‌های مهم"
    )

    # -----------------------------------------------------
    # سابقه خانوادگی
    # -----------------------------------------------------

    st.header("۶. سابقه خانوادگی")

    family_cvd = yes_no(
        "آیا سابقه بیماری قلبی-عروقی در خانواده وجود دارد؟"
    )

    family_mi = yes_no(
        "آیا سابقه سکته قلبی در خانواده وجود دارد؟"
    )

    sudden_death = yes_no(
        "آیا سابقه مرگ ناگهانی قلبی در خانواده وجود دارد؟"
    )

    family_other = st.text_area(
        "سایر موارد مهم در سابقه خانوادگی"
    )

    # -----------------------------------------------------
    # سبک زندگی
    # -----------------------------------------------------

    st.header("۷. سبک زندگی")

    c1, c2 = st.columns(2)

    with c1:

        smoking = yes_no(
            "آیا بیمار سیگار مصرف می‌کند؟"
        )

        cigarettes = st.number_input(
            "تعداد نخ سیگار در روز",
            min_value=0,
            value=0
        )

        smoking_years = st.number_input(
            "تعداد سال‌های مصرف سیگار",
            min_value=0,
            value=0
        )

        hookah = yes_no(
            "آیا قلیان مصرف می‌کند؟"
        )

        alcohol = yes_no(
            "آیا الکل مصرف می‌کند؟"
        )

    with c2:

        exercise = st.text_area(
            "میزان فعالیت و ورزش"
        )

        diet = st.text_area(
            "وضعیت و نوع رژیم غذایی"
        )

        sleep = st.text_area(
            "وضعیت خواب"
        )

    # -----------------------------------------------------
    # داروها
    # -----------------------------------------------------

    st.header("۸. داروها")

    medications = st.text_area(
        "داروهای مصرفی فعلی؛ نام، مقدار و تعداد مصرف"
    )

    allergies = st.text_area(
        "حساسیت‌های دارویی"
    )

    adherence = st.text_area(
        "آیا بیمار داروهای خود را نامنظم مصرف می‌کند یا اخیراً دارویی را قطع کرده است؟"
    )

    # -----------------------------------------------------
    # آزمایش‌ها
    # -----------------------------------------------------

    st.header("۹. نتایج آزمایش‌ها و بررسی‌های قبلی")

    c1, c2, c3 = st.columns(3)

    with c1:

        blood_pressure = st.text_input(
            "فشار خون"
        )

        heart_rate = st.text_input(
            "ضربان قلب"
        )

        oxygen = st.text_input(
            "اشباع اکسیژن خون"
        )

        ecg = st.text_area(
            "نتیجه نوار قلب ECG"
        )

    with c2:

        echo = st.text_area(
            "نتیجه اکوکاردیوگرافی"
        )

        holter = st.text_area(
            "نتیجه هولتر"
        )

        stress_test = st.text_area(
            "نتیجه تست ورزش"
        )

    with c3:

        coronary_imaging = st.text_area(
            "نتیجه CT کرونر یا آنژیوگرافی"
        )

        labs = st.text_area(
            "نتایج آزمایش خون"
        )

        other_tests = st.text_area(
            "سایر گزارش‌ها و بررسی‌ها"
        )

    # -----------------------------------------------------
    # سؤال پزشک
    # -----------------------------------------------------

    st.header("۱۰. سؤال یا درخواست پزشک")

    clinical_question = st.text_area(
        "پزشک دقیقاً می‌خواهد چه موضوعی را بررسی کند؟",
        height=120
    )

    # -----------------------------------------------------
    # Submit
    # -----------------------------------------------------

    submitted = st.form_submit_button(
        "🧠 تولید پرامپت برای ChatGPT",
        use_container_width=True
    )


# =========================================================
# OUTPUT
# =========================================================

if submitted:

    data = {

        "age": age,
        "sex": sex,
        "height": height,
        "weight": weight,
        "occupation": clean(occupation),

        "chief_complaint": clean(chief_complaint),
        "onset": clean(onset),
        "frequency": clean(frequency),

        "chest_pain": chest_pain,
        "pain_location": clean(pain_location),
        "pain_type": ", ".join(pain_type),
        "pain_intensity": pain_intensity,
        "pain_duration": clean(pain_duration),
        "radiation": clean(radiation),
        "activity_trigger": activity_trigger,
        "rest_relief": rest_relief,
        "breathing_change": breathing_change,
        "movement_change": movement_change,

        "dyspnea": dyspnea,
        "palpitations": palpitations,
        "dizziness": dizziness,
        "syncope": syncope,
        "sweating": sweating,
        "nausea": nausea,
        "fatigue": fatigue,
        "edema": edema,
        "orthopnea": orthopnea,
        "pnd": pnd,

        "hypertension": hypertension,
        "diabetes": diabetes,
        "hyperlipidemia": hyperlipidemia,
        "kidney_disease": kidney_disease,
        "thyroid": thyroid,
        "previous_mi": previous_mi,
        "stroke": stroke,
        "cad": cad,
        "angiography": angiography,
        "bypass": bypass,
        "arrhythmia": arrhythmia,
        "valvular": valvular,
        "congenital": congenital,
        "other_conditions": clean(other_conditions),

        "family_cvd": family_cvd,
        "family_mi": family_mi,
        "sudden_death": sudden_death,
        "family_other": clean(family_other),

        "smoking": smoking,
        "cigarettes": cigarettes,
        "smoking_years": smoking_years,
        "hookah": hookah,
        "alcohol": alcohol,
        "exercise": clean(exercise),
        "diet": clean(diet),
        "sleep": clean(sleep),

        "medications": clean(medications),
        "allergies": clean(allergies),
        "adherence": clean(adherence),

        "blood_pressure": clean(blood_pressure),
        "heart_rate": clean(heart_rate),
        "oxygen": clean(oxygen),
        "ecg": clean(ecg),
        "echo": clean(echo),
        "holter": clean(holter),
        "stress_test": clean(stress_test),
        "coronary_imaging": clean(coronary_imaging),
        "labs": clean(labs),
        "other_tests": clean(other_tests),

        "clinical_question": clean(clinical_question)
    }

    final_prompt = build_prompt(data)

    st.success(
        "پرامپت با موفقیت تولید شد."
    )

    st.header(
        "📋 پرامپت آماده برای ChatGPT"
    )

    st.info(
        "متن زیر را کامل کپی کنید و در ChatGPT قرار دهید."
    )

    st.text_area(
        "پرامپت تولیدشده",
        value=final_prompt,
        height=700
    )

    st.download_button(
        label="⬇️ دانلود پرامپت به صورت فایل TXT",
        data=final_prompt,
        file_name="cardiology_patient_prompt.txt",
        mime="text/plain",
        use_container_width=True
    )