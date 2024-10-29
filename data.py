import json
import os

class DataManager:
    def __init__(self):
        self.questions_file = 'questions.json'
        self.resources_file = 'resources.txt'
        self.questions = self.load_questions()

    def load_questions(self):
        if os.path.exists(self.questions_file):
            with open(self.questions_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Carica le domande predefinite
            return self.default_questions()

    def default_questions(self):
        # Domande predefinite basate sull'AI ACT
        questions = [
            {
                'id': 1,
                'question': "Il sistema IA manipola il comportamento umano in modo subliminale?",
                'level': "Rischio Inaccettabile",
                'criteria': "Manipolazione Subliminale",
                'suggestion': "Evitare pratiche che manipolano il subconscio degli utenti."
            },
            {
                'id': 2,
                'question': "Il sistema IA sfrutta vulnerabilità di gruppi specifici (es. bambini, persone con disabilità)?",
                'level': "Rischio Inaccettabile",
                'criteria': "Sfruttamento delle Vulnerabilità",
                'suggestion': "Proteggere i gruppi vulnerabili evitando lo sfruttamento delle loro vulnerabilità."
            },
            {
                'id': 3,
                'question': "Il sistema IA è utilizzato per il punteggio sociale da parte delle autorità pubbliche?",
                'level': "Rischio Inaccettabile",
                'criteria': "Punteggio Sociale",
                'suggestion': "Evitare sistemi di punteggio sociale che possono discriminare gli individui."
            },
            {
                'id': 4,
                'question': "Il sistema IA prevede l'uso di sorveglianza biometrica di massa in spazi pubblici?",
                'level': "Rischio Inaccettabile",
                'criteria': "Sorveglianza di Massa",
                'suggestion': "Evitare l'uso di tecnologie di sorveglianza biometrica di massa."
            },
            {
                'id': 5,
                'question': "Il sistema IA è un componente di sicurezza in prodotti regolamentati da normative UE?",
                'level': "Rischio Alto",
                'criteria': "Allegato II",
                'suggestion': "Assicurarsi che il sistema soddisfi gli standard di sicurezza applicabili."
            },
            {
                'id': 6,
                'question': "Il sistema IA è utilizzato per l'identificazione biometrica o il riconoscimento facciale in spazi pubblici?",
                'level': "Rischio Alto",
                'criteria': "Identificazione Biometrica",
                'suggestion': "Implementare rigorose misure di privacy e sicurezza."
            },
            {
                'id': 7,
                'question': "Il sistema IA è utilizzato nella gestione di infrastrutture critiche (es. reti energetiche, idriche)?",
                'level': "Rischio Alto",
                'criteria': "Gestione Infrastrutture Critiche",
                'suggestion': "Garantire l'affidabilità e la robustezza del sistema."
            },
            {
                'id': 8,
                'question': "Il sistema IA determina l'accesso all'istruzione o alla formazione professionale?",
                'level': "Rischio Alto",
                'criteria': "Istruzione e Formazione",
                'suggestion': "Assicurare equità e trasparenza nei processi decisionali."
            },
            {
                'id': 9,
                'question': "Il sistema IA è utilizzato per la selezione del personale o valutazione delle prestazioni?",
                'level': "Rischio Alto",
                'criteria': "Occupazione",
                'suggestion': "Evitare bias e discriminazioni nel processo di selezione."
            },
            {
                'id': 10,
                'question': "Il sistema IA determina l'accesso a servizi pubblici essenziali o benefici sociali?",
                'level': "Rischio Alto",
                'criteria': "Servizi Pubblici Essenziali",
                'suggestion': "Garantire trasparenza e correttezza nelle decisioni."
            },
            {
                'id': 11,
                'question': "Il sistema IA è utilizzato per la profilazione predittiva nelle forze dell'ordine?",
                'level': "Rischio Alto",
                'criteria': "Forze dell'Ordine",
                'suggestion': "Implementare controlli per prevenire abusi e discriminazioni."
            },
            {
                'id': 12,
                'question': "Il sistema IA valuta richieste di asilo o migrazione?",
                'level': "Rischio Alto",
                'criteria': "Migrazione e Asilo",
                'suggestion': "Assicurare che i diritti fondamentali siano rispettati."
            },
            {
                'id': 13,
                'question': "Il sistema IA assiste nelle decisioni giudiziarie o nei processi democratici?",
                'level': "Rischio Alto",
                'criteria': "Giustizia e Processi Democratici",
                'suggestion': "Mantenere l'integrità e l'imparzialità del sistema."
            },
            {
                'id': 14,
                'question': "Il sistema IA ha un impatto moderato su privacy, sicurezza o diritti fondamentali?",
                'level': "Rischio Moderato",
                'criteria': "Impatto Moderato",
                'suggestion': "Implementare misure di trasparenza e gestione dei consensi."
            },
            {
                'id': 15,
                'question': "Il sistema IA ha un impatto minimo sui diritti fondamentali o sulla sicurezza?",
                'level': "Rischio Basso",
                'criteria': "Impatto Minimo",
                'suggestion': "Continuare a monitorare e migliorare il sistema."
            }
        ]
        return questions

    def evaluate_risk(self, answers):
        # Valuta il rischio dopo aver analizzato tutte le risposte
        risk_levels = {
            "Rischio Inaccettabile": False,
            "Rischio Alto": False,
            "Rischio Moderato": False,
            "Rischio Basso": True  # Predefinito a vero, verrà modificato se necessario
        }

        criteria = []
        suggestions = []

        for ans in answers:
            if ans['response']:
                q = next((item for item in self.questions if item['id'] == ans['id']), None)
                if q:
                    level = q['level']
                    risk_levels["Rischio Basso"] = False  # Se c'è almeno una risposta 'Sì', non è più rischio basso
                    if level == "Rischio Inaccettabile":
                        risk_levels["Rischio Inaccettabile"] = True
                    elif level == "Rischio Alto" and not risk_levels["Rischio Inaccettabile"]:
                        risk_levels["Rischio Alto"] = True
                    elif level == "Rischio Moderato" and not risk_levels["Rischio Inaccettabile"] and not risk_levels["Rischio Alto"]:
                        risk_levels["Rischio Moderato"] = True

                    criteria.append(q['criteria'])
                    suggestions.append(q.get('suggestion', ''))

        if risk_levels["Rischio Inaccettabile"]:
            return "Rischio Inaccettabile", ", ".join(criteria), "\n".join(suggestions)
        elif risk_levels["Rischio Alto"]:
            return "Rischio Alto", ", ".join(criteria), "\n".join(suggestions)
        elif risk_levels["Rischio Moderato"]:
            return "Rischio Moderato", ", ".join(criteria), "\n".join(suggestions)
        else:
            return "Rischio Basso", "Nessun criterio ad alto rischio soddisfatto", "Considera di implementare misure di sicurezza di base."

    def get_requirements(self, level):
        # Restituisce i requisiti in base al livello di rischio
        requirements = {
            "Rischio Inaccettabile": "Questo sistema IA è vietato secondo l'AI ACT.",
            "Rischio Alto": (
                "Requisiti da soddisfare:\n"
                "- Sistema di gestione del rischio\n"
                "- Qualità dei dati e governance\n"
                "- Documentazione tecnica\n"
                "- Registrazione degli eventi\n"
                "- Trasparenza e informazioni agli utilizzatori\n"
                "- Supervisione umana\n"
                "- Accuratezza, robustezza e sicurezza informatica\n"
            ),
            "Rischio Moderato": (
                "Requisiti da soddisfare:\n"
                "- Trasparenza\n"
                "- Monitoraggio dell'utilizzo\n"
                "- Gestione dei consensi\n"
            ),
            "Rischio Basso": (
                "Requisiti da soddisfare:\n"
                "- Revisione periodica\n"
                "- Formazione di base agli utilizzatori\n"
            )
        }
        return requirements.get(level, "")

    def get_resources(self):
        if os.path.exists(self.resources_file):
            with open(self.resources_file, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return "Risorse non disponibili."

    def save_assessment(self, file_path, data):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_assessment(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return None
