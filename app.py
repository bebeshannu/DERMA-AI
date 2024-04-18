from flask import Flask, render_template, request,send_from_directory
from fastai.vision.all import *
import pathlib
import os
from flask import redirect, url_for



# Replace PosixPath with WindowsPath temporarily for Windows compatibility
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Initialize Flask app
app = Flask(__name__)

# Define path to the trained model
path = r"D:\Github\DERMAAI\densenet1212.pkl"


# Load the trained model
model = load_learner(path, cpu=True)

# Restore PosixPath
pathlib.PosixPath = temp

# Define routes
@app.route('/')
def form():
    return render_template('index.html')


@app.route('/bowen')
def bowen():
    return send_from_directory('templates', 'bowen.html')

@app.route('/chickenpox')
def chickenpox():
    return send_from_directory('templates', 'chickenpox.html')

@app.route('/chiggers')
def chiggers():
    return send_from_directory('templates', 'chiggers.html')

@app.route('/dermatofibroma')
def dermatofibroma():
    return send_from_directory('templates', 'dermatofibroma.html')

@app.route('/eczema')
def eczema():
    return send_from_directory('templates', 'eczema.html')

@app.route('/enterovirus')
def enterovirus():
    return send_from_directory('templates', 'enterovirus.html')

@app.route('/keratosis')
def keratosis():
    return send_from_directory('templates', 'keratosis.html')

@app.route('/measles')
def measles():
    return send_from_directory('templates', 'measles.html')

@app.route('/normal_skin')
def normal_skin():
    return send_from_directory('templates', 'normal_skin.html')

@app.route('/ringworm')
def ringworm():
    return send_from_directory('templates', 'ringworm.html')

@app.route('/scabies')
def scabies():
    return send_from_directory('templates', 'scabies.html')

@app.route('/psoriasis')
def psoriasis():
    return send_from_directory('templates', 'psoriasis.html')




@app.route('/upload', methods=["POST"])
def upload():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file part"
        
        file = request.files['image']

        if file.filename == '':
            return "No selected file"
        
        if file:
            filename = file.filename
            file.save(filename)
            prediction = model.predict(filename)[0]
            rec = ""
            rec2 = ""
            rec3 = ""
            rec4 = ""
            rec5 = ""
            sources = "static/img/"

            if prediction == "Bowens":
                prediction = "Bowens"
                rec = """Overview:
                Bowen's disease is a type of squamous cell carcinoma in situ, a noninvasive form of skin cancer. It typically appears as a red, scaly patch on the skin, often resembling eczema or psoriasis. Bowen's disease primarily affects areas of the skin that are frequently exposed to the sun, such as the face, scalp, hands, and lower legs. The exact cause of Bowen's disease is not fully understood, but it is believed to be linked to prolonged sun exposure, aging, and certain genetic factors."""
                rec2 = """Diagnosis:
Diagnosing Bowen's disease usually involves a thorough physical examination by a dermatologist. A skin biopsy may be performed to confirm the diagnosis, where a small sample of the affected skin is removed and examined under a microscope. Additional tests, such as dermoscopy or imaging studies, may be recommended in some cases to assess the extent of the disease."""
                rec3 = """Treatment options for Bowen's disease depend on various factors, including the size and location of the lesion, as well as the individual's overall health. Common treatment modalities include:Topical therapies, Cryotherapy, Surgical excision, Photodynamic therapy, Laser therapy, Radiation therapy."""
                rec4 = """Personalized Care Recommendations:
Individuals diagnosed with Bowen's disease should receive personalized care recommendations tailored to their specific medical history, the extent of the disease, and any underlying health conditions. This may include a detailed treatment plan outlining the chosen therapy, follow-up appointments for monitoring, and lifestyle recommendations such as sun protection measures and smoking cessation."""
                sources += "bowens.jpg"
            # Add other conditions similarly
            
            elif prediction == "Chickenpox":
                prediction = "Chickenpox"
                rec = """Overview:
                Chickenpox, also known as varicella, is a highly contagious viral infection caused by the varicella-zoster virus (VZV). It primarily affects children but can also occur in adults who have not been previously infected or vaccinated against the virus. Chickenpox is characterized by an itchy rash consisting of small, red bumps that progress into fluid-filled blisters before crusting over and healing. The rash typically appears first on the face, chest, and back, then spreads to other parts of the body."""
                rec2 = """Transmission:
Chickenpox is highly contagious and spreads from person to person through respiratory droplets or direct contact with the fluid from the blisters of an infected person. The virus can also be transmitted through airborne particles from coughing or sneezing."""
                rec3 = """ Treatment:
Treatment for chickenpox is primarily supportive and aimed at relieving symptoms. This may include:
Over-the-counter antihistamines or calamine lotion to relieve itching, 
Acetaminophen (paracetamol) to reduce fever and relieve discomfort ,
Avoiding scratching to prevent bacterial infection and scarring, 
Rest and hydration to help the body recover, 
In severe cases or for individuals at high risk of complications, antiviral medications such as acyclovir may be prescribed."""
                rec4 = """Prevention:
The most effective way to prevent chickenpox is through vaccination. The chickenpox vaccine is routinely recommended for children and adults who have not had chickenpox or been vaccinated previously. Vaccination not only protects individuals from contracting chickenpox but also helps prevent the spread of the virus within communities, particularly to those at higher risk of complications."""
                sources += "chickenpox.jpg"
                
            elif prediction == "Dermatofibroma":
                prediction = "Dermatofibroma"
                rec = """Dermatofibroma is a common benign skin growth that often appears as a small, firm bump on the skin. It is 
            typically painless and may range in color from pink to brown or black. Dermatofibromas often develop on the legs, but they 
            can occur anywhere on the body."""
                rec2 = """If you have a dermatofibroma, it is usually not a cause for concern. However, if you notice any changes in size, 
            color, or texture of the bump, or if it becomes painful or starts to bleed, you should consult a dermatologist for further 
            evaluation."""
                rec3 = """Treatment for dermatofibroma is generally not necessary unless it is causing discomfort or is in a location 
            where it may be easily irritated or prone to injury. If treatment is desired, options may include surgical removal, 
            cryotherapy, or laser therapy."""
                rec4 = """While there is no known way to prevent dermatofibromas from developing, protecting your skin from excessive sun 
            exposure and avoiding injury to the skin may help reduce the risk of developing these growths. Regular skin checks with a 
            dermatologist can also help detect any changes in the skin and allow for early intervention if necessary."""
                sources += "dermatofibroma.png"
            elif prediction == "Chiggers":
                prediction = "Chiggers"
                rec = """Looks like the rashes you have on your skin are Chigger Bites"""
                rec2 = """Overview:
Chiggers are not insects; they are arachnids, closely related to spiders and ticks. These mites are barely visible to the naked eye and typically measure around 0.15 to 0.3 millimeters in size. Chiggers go through four stages in their lifecycle: egg, larva, nymph, and adult. It's the larvae stage that commonly causes problems for humans.

Bite and Feeding:
Chigger larvae attach themselves to the skin of mammals, including humans, to feed on their skin cells. Contrary to popular belief, chiggers do not burrow into the skin or suck blood. Instead, they inject enzymes into the skin that cause the surrounding tissue to break down. The chiggers then feed on the liquefied skin cells. Chigger bites often occur in areas where clothing fits tightly against the skin, such as around the ankles, waistband, or areas with thin skin."""
                rec3 = """ISymptoms:
After a chigger bite, symptoms typically develop within a few hours. Common signs and symptoms include:

Intense itching,
Red, raised bumps or welts,
Skin irritation and inflammation,
Occasionally, a visible feeding tube (stylostome) may be seen at the center of the bite."""
                rec4 = """Treatment:
Treatment for chigger bites focuses on relieving symptoms and preventing infection. Some recommended measures include:

Washing the affected area with soap and water to remove any remaining chiggers and reduce the risk of infection.
Applying calamine lotion, hydrocortisone cream, or other anti-itch creams to alleviate itching and inflammation.
Taking oral antihistamines to reduce itching and discomfort.
Avoiding scratching the bites to prevent secondary bacterial infections and scarring."""
                rec5 = """Prevention:
Preventing chigger bites involves taking precautions when spending time outdoors, especially in areas where chiggers are prevalent. Some preventive measures include:

Wearing long sleeves, pants, and closed-toe shoes when hiking or walking in grassy or wooded areas.
Tucking pants into socks and applying insect repellents containing DEET or permethrin to clothing and exposed skin.
Showering promptly after outdoor activities to remove any chiggers that may be on the skin.
Laundering clothing in hot water and drying them on high heat to kill any chiggers that may be present."""
                sources += "chiggers.png"
            elif prediction == "Enterovirus":
                prediction = "Enterovirus"
                rec = """Looks like the rashes you have is a symptom of Enterovirus!!"""
                rec2 = """Enteroviruses are a group of viruses that belong to the Picornaviridae family, which includes polioviruses, coxsackieviruses, echoviruses, and other related viruses. These viruses are common and can cause a wide range of illnesses, ranging from mild to severe, including respiratory infections, gastrointestinal illnesses, and neurological diseases."""
                rec3 = """ransmission:
Enteroviruses are primarily spread through close contact with an infected person or by contact with contaminated surfaces, objects, or food. The viruses can be shed in the stool or respiratory secretions of infected individuals, allowing for easy transmission to others."""
                rec4 = """Symptoms:
The symptoms of enterovirus infections can vary depending on the specific virus involved and the individual's age and immune status. Common symptoms may include:

Fever
Respiratory symptoms such as cough, runny nose, and sore throat
Gastrointestinal symptoms such as nausea, vomiting, diarrhea, and abdominal pain
Skin rash (in the case of hand, foot, and mouth disease)
Headache
Muscle aches
Neurological symptoms such as meningitis or encephalitis in severe cases"""
                rec5 = """TTreatment:
There is no specific antiviral treatment for most enterovirus infections. Treatment typically focuses on relieving symptoms and providing supportive care, such as:

Rest
Fluids to prevent dehydration,
Over-the-counter medications to reduce fever and alleviate pain or discomfort,
In severe cases or complications such as meningitis or encephalitis, hospitalization and supportive care may be necessary."""
                sources += "enterovirus.png"
            elif prediction == "Keratosis":
                prediction = "Keratosis"
                rec = """Pigmented benign keratosis, also known as seborrheic keratosis, is a common benign skin growth that typically 
            appears as a waxy, raised bump or patch on the skin. These growths are often brown or black and may appear on any part of 
            the body."""
                rec2 = """If you have a pigmented benign keratosis, it is usually not a cause for concern. However, if you notice any 
            changes in size, color, or texture of the growth, or if it becomes painful or starts to bleed, you should consult a 
            dermatologist for further evaluation."""
                rec3 = """Treatment for pigmented benign keratosis is generally not necessary unless the growth is causing discomfort or 
            is in a location where it may be easily irritated or prone to injury. If treatment is desired, options may include 
            surgical removal, cryotherapy, or laser therapy."""
                rec4 = """While there is no known way to prevent pigmented benign keratosis from developing, protecting your skin from 
            excessive sun exposure and avoiding injury to the skin may help reduce the risk of developing these growths. Regular skin
            checks with a dermatologist can also help detect any changes in the skin and allow for early intervention if necessary."""
                sources += "pigmented-benign-keratosis.png"
            elif prediction == "Eczema":
                prediction = "Eczema"
                rec = """Overview:
                Eczema, also known as atopic dermatitis, is a common chronic skin condition characterized by inflammation and itching. It can affect people of all ages but is particularly common in infants and young children. Eczema tends to occur in flare-ups, with periods of exacerbation followed by periods of remission. While there is no cure for eczema, various treatments can help manage symptoms and improve quality of life."""
                rec2 = """Symptoms:
The symptoms of eczema can vary from person to person and may include:

Dry, red, and inflamed skin,
Itching, which can be intense and may worsen at night,
Rough or scaly patches of skin,
Small, raised bumps that may ooze or crust over when scratched,
Thickened, cracked, or leathery skin in chronic cases,
Skin discoloration or changes in pigmentation,
Secondary infections due to scratching and broken skin."""
                rec3 = """Causes and Triggers:
The exact cause of eczema is not fully understood, but it is believed to involve a combination of genetic, environmental, and immune factors. Certain triggers can exacerbate eczema symptoms, including:

Dry skin
Irritants such as soaps, detergents, and harsh chemicals,
Allergens such as dust mites, pet dander, pollen, and certain foods,
Heat and sweating,
Stress,
Hormonal changes,
Microbial infections."""
                rec4 = """Treatment:
Treatment for eczema aims to relieve symptoms, reduce inflammation, and prevent flare-ups. Common treatment options may include: Moisturizers, Topical corticosteroids,  Topical calcineurin inhibitors, Antihistamines, Wet wrap therapy, Avoiding triggers."""
                sources += "eczema.jpg"
            elif prediction == "Psoriasis":
                prediction = "Psoriasis"
                rec = """Psoriasis is a chronic autoimmune skin condition that causes rapid skin cell turnover, resulting in the formation of thick, red, scaly patches on the skin's surface. These patches, known as plaques, can appear anywhere on the body but commonly affect the elbows, knees, scalp, and lower back. Psoriasis is not contagious but can significantly impact a person's physical and emotional well-being."""
                rec2 = """Symptoms:
The symptoms of psoriasis can vary widely among individuals and may include:

Red, raised patches of skin covered with silvery scales (plaques),
Itching, burning, or soreness in affected areas,
Dry, cracked skin that may bleed,
Thickened, pitted, or ridged nails,
Joint pain, stiffness, or swelling (psoriatic arthritis)."""
                rec3 = """Causes and Triggers:
The exact cause of psoriasis is not fully understood, but it is believed to involve a combination of genetic, immune, and environmental factors. Certain triggers can exacerbate psoriasis symptoms or lead to flare-ups, including:

Stress,
Infections, particularly streptococcal infections,
Injury to the skin, such as cuts, scrapes, or sunburns,
Medications, including certain antimalarial drugs, beta-blockers, and lithium,
Smoking and excessive alcohol consumption,
Hormonal changes, such as those during puberty or menopause."""
                rec4 = """Treatment:
Treatment for psoriasis aims to reduce inflammation, slow down skin cell turnover, and alleviate symptoms. Treatment options may include:Topical treatments, Phototherapy, Systemic Medications,  Lifestyle modifications."""
                sources += "Psoriasis.jpg"
            elif prediction == "Ringworm":
                prediction = "Ringworm"
                rec = "Overview: Ringworm, also known as dermatophytosis or tinea corporis, is a contagious fungal infection that typically presents as a red, circular rash with clear skin in the center, resembling a ring. It is called ringworm due to the ring-like appearance of the rash, although no worm is involved in the infection. Ringworm can affect people of all ages and is highly contagious, spreading through direct contact with an infected person or animal, or by sharing contaminated items such as clothing, towels, or sports equipment."""
                rec2 = "Symptoms:The symptoms of ringworm may vary depending on the location of the infection but commonly include:Red, circular rash with raised edges,Itching, burning, or discomfort in the affected area,Scaling, flaking, or cracking of the skin,Hair loss (in cases of scalp ringworm),In severe cases, the rash may blister or ooze fluid."
                rec3 = "Treatment:Treatment for ringworm typically involves antifungal medications, which may be applied topically as creams, ointments, or sprays for mild cases or taken orally for more severe or widespread infections. Common antifungal medications include clotrimazole, miconazole, terbinafine, and ketoconazole. It's essential to continue treatment for the prescribed duration, even after symptoms improve, to ensure the infection is fully eradicated and prevent recurrence."
                rec4 = "If you suspect you have ringworm or are experiencing symptoms of a fungal infection, it's essential to consult a healthcare professional or dermatologist for an accurate diagnosis and appropriate treatment. Early intervention can help alleviate symptoms and prevent the spread of the infection to others."
                sources += "Ringworm.jpg"
            elif prediction == "Scabies":
                prediction = "Scabies"
                rec = "Overview: Scabies is caused by the Sarcoptes scabiei mite, which burrows into the skin and lays eggs. The infestation leads to an allergic reaction, resulting in itching and a rash. Scabies is highly contagious and spreads through close personal contact, such as skin-to-skin contact, or by sharing bedding, clothing, or towels with an infested person."
                rec2 = "Symptoms: The symptoms of scabies typically include Intense itching, which may worsen at night or after a hot shower. A pimple-like rash, often with tiny blisters or burrow tracks (thin, irregular lines) in the skin. Sores or abrasions caused by scratching, can lead to bacterial infections in severe cases. The rash may appear on various parts of the body, including the wrists, elbows, armpits, waist, genital area, buttocks, and between the fingers."
                rec3 = "Diagnosis: Diagnosing scabies often involves a physical examination by a healthcare professional. The characteristic appearance of the rash and the presence of burrow tracks may suggest scabies. In some cases, a skin scraping may be performed to examine under a microscope for the presence of mites, eggs, or fecal matter."
                rec4 = "Treatment: Treatment for scabies typically involves the use of prescription medications to kill the mites and eggs and relieve symptoms. Commonly prescribed treatments include Topical scabicidal medications, Oral medications, Antihistamines etc."
                rec5 = "Prevention:To prevent the spread of scabies, it's important to avoid close contact with infested individuals and their personal belongings. If you suspect you have scabies or have been in close contact with someone who does, it's essential to seek medical attention promptly for diagnosis and treatment.Overall, scabies is a treatable condition, but prompt and thorough treatment is necessary to eradicate the infestation and prevent reinfestation."
                sources += "Scabies.jpg"
            elif prediction == "Normal Skin":
                prediction = "Normal Skin"
                rec = "Looks like you have Normal Skin! Having normal skin is a wonderful thing! It means your skin is healthy, balanced, and doesn't require special attention or worry. "
               
                sources += "Normal.jpg"
            elif prediction == "Measles":
                prediction = "Measles"
                rec = "Looks like the rash you have is a symptom of Measles"
                rec2 = "Overview: Measles is caused by the measles virus, which belongs to the Paramyxoviridae family. It spreads through respiratory droplets from coughing or sneezing of an infected person and can also be transmitted through direct contact with nasal or throat secretions. Measles is highly contagious and can lead to serious complications, especially in young children, pregnant women, and individuals with weakened immune systems."
                rec3 = """Symptoms:
The symptoms of measles typically appear in two stages:

Early symptoms (Prodrome):
Fever,b
Runny nose,
Cough,
Red, watery eyes (conjunctivitis)
Characteristic rash:
A red, blotchy rash typically begins a few days after the onset of early symptoms.
The rash usually starts on the face and spreads downward to the rest of the body over several days.
The rash may be accompanied by high fever, which can spike to 104°F (40°C) or higher."""
                rec4 = """Treatment:
There is no specific antiviral treatment for measles. Treatment typically focuses on relieving symptoms and managing complications. Some general recommendations may include:

Rest and hydration to help the body recover.
Acetaminophen (paracetamol) to reduce fever and relieve discomfort.
Vitamin A supplementation, which has been shown to reduce the risk of complications, especially in children with vitamin A deficiency.
Antibiotics may be prescribed for secondary bacterial infections such as pneumonia or ear infections."""
                rec5 = """Prevention:
The most effective way to prevent measles is through vaccination. The measles vaccine, usually administered as part of the measles, mumps, and rubella (MMR) vaccine, is highly effective at preventing measles infection. The MMR vaccine is typically given in two doses, with the first dose administered at 12-15 months of age and the second dose at 4-6 years of age. Vaccination not only protects individuals from measles but also helps prevent the spread of the virus within communities, contributing to herd immunity.

Overall, measles is a highly contagious viral infection that can lead to serious complications, especially in vulnerable populations. Vaccination is the most effective way to prevent measles and its associated complications. If you suspect you or someone else has measles, it's essential to seek medical attention promptly for diagnosis and appropriate management."""
                sources += "Measles.jpg"
            
            return render_template('results.html', prediction=prediction, sources=sources, rec=rec, rec2=rec2, rec3=rec3, rec4=rec4, rec5=rec5)

if __name__ == '__main__':
    app.run(debug=True)
