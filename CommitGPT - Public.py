import os
import openai
from git import Repo
from dotenv import load_dotenv

# Load .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")

# Prompt pour générer le résumé des modifications
summary_context = "Tu es un expert en développement informatique. Tu reçois des modifications d'un projet et tu génères un résumé des modifications effectuées. Ta réponse doit uniquement être le résumé des modifications en 1 phrase, sans superflu."

# Prompt pour générer le message de commit
commit_context = "DOCUMENTATION : [['🎨', ':art:', 'Améliorer la structure / le format du code.'], ['⚡️', ':zap:', 'Améliorer les performances.'], ['🔥', ':fire:', 'Supprimer du code ou des fichiers.'], ['🐛', ':bug:', 'Corriger un bug.'], ['🚑️', ':ambulance:', 'Correction critique.'], ['✨', ':sparkles:', 'Introduire de nouvelles fonctionnalités.'], ['📝', ':memo:', 'Ajouter ou mettre à jour la documentation.'], ['🚀', ':rocket:', 'Déployer des choses.'], ['💄', ':lipstick:', 'Ajouter ou mettre à jour l'interface utilisateur et les fichiers de style.'], ['🎉', ':tada:', 'Commencer un projet.'], ['✅', ':white_check_mark:', 'Ajouter, mettre à jour ou passer des tests.'], ['🔒️', ':lock:', 'Corriger des problèmes de sécurité.'], ['🔐', ':closed_lock_with_key:', 'Ajouter ou mettre à jour des secrets.'], ['🔖', ':bookmark:', 'Tags de version / de publication.'], ['🚨', ':rotating_light:', 'Corriger les avertissements du compilateur / du linter.'], ['🚧', ':construction:', 'Travail en cours.'], ['💚', ':green_heart:', 'Corriger la construction CI.'], ['⬇️', ':arrow_down:', 'Réduire les dépendances.'], ['⬆️', ':arrow_up:', 'Mettre à jour les dépendances.'], ['📌', ':pushpin:', 'Épingler les dépendances à des versions spécifiques.'], ['👷', ':construction_worker:', 'Ajouter ou mettre à jour le système de construction CI.'], ['📈', ':chart_with_upwards_trend:', 'Ajouter ou mettre à jour des analyses ou suivre le code.'], ['♻️', ':recycle:', 'Refactoriser le code.'], ['➕', ':heavy_plus_sign:', 'Ajouter une dépendance.'], ['➖', ':heavy_minus_sign:', 'Supprimer une dépendance.'], ['🔧', ':wrench:', 'Ajouter ou mettre à jour des fichiers de configuration.'], ['🔨', ':hammer:', 'Ajouter ou mettre à jour des scripts de développement.'], ['🌐', ':globe_with_meridians:', 'Internationalisation et localisation.'], ['✏️', ':pencil2:', 'Corriger les fautes de frappe.'], ['💩', ':poop:', 'Écrire un code incorrect qui doit être amélioré.'], ['⏪️', ':rewind:', 'Annuler les modifications.'], ['🔀', ':twisted_rightwards_arrows:', 'Fusionner des branches.'], ['📦️', ':package:', 'Ajouter ou mettre à jour des fichiers ou des packages compilés.'], ['👽️', ':alien:', 'Mettre à jour le code en raison de modifications d'API externes.'], ['🚚', ':truck:', 'Déplacer ou renommer des ressources (par ex. : fichiers, chemins, routes).'], ['📄', ':page_facing_up:', 'Ajouter ou mettre à jour une licence.'], ['💥', ':boom:', 'Introduire des modifications importantes.'], ['🍱', ':bento:', 'Ajouter ou mettre à jour des ressources.'], ['♿️', ':wheelchair:', 'Améliorer l'accessibilité.'], ['💡', ':bulb:', 'Ajouter ou mettre à jour des commentaires dans le code source.'], ['🍻', ':beers:', 'Coder en étant ivre.'], ['💬', ':speech_balloon:', 'Ajouter ou mettre à jour du texte et des littéraux.'], ['🗃️', ':card_file_box:', 'Effectuer des modifications liées à la base de données.'], ['🔊', ':loud_sound:', 'Ajouter ou mettre à jour des journaux.'], ['🔇', ':mute:', 'Supprimer des journaux.'], ['👥', ':busts_in_silhouette:', 'Ajouter ou mettre à jour le(s) contributeur(s).'], ['🚸', ':children_crossing:', 'Améliorer l'expérience utilisateur / l'utilisabilité.'], ['🏗️', ':building_construction:', 'Effectuer des modifications architecturales.'], ['📱', ':iphone:', 'Travailler sur la conception responsive.'], ['🤡', ':clown_face:', 'Simuler des choses.'], ['🥚', ':egg:', 'Ajouter ou mettre à jour un easter egg.'], ['🙈', ':see_no_evil:', 'Ajouter ou mettre à jour un fichier .gitignore.'], ['📸', ':camera_flash:', 'Ajouter ou mettre à jour des captures d'écran.'], ['⚗️', ':alembic:', 'Effectuer des expériences.'], ['🔍️', ':mag:', 'Améliorer le référencement.'], ['🏷️', ':label:', 'Ajouter ou mettre à jour des types.'], ['🌱', ':seedling:', 'Ajouter ou mettre à jour des fichiers de données initiales.'], ['🚩', ':triangular_flag_on_post:', 'Ajouter, mettre à jour ou supprimer des indicateurs de fonctionnalités.'], ['🥅', ':goal_net:', 'Attraper les erreurs.'], ['💫', ':dizzy:', 'Ajouter ou mettre à jour des animations et des transitions.'], ['🗑️', ':wastebasket:', 'Déprécier le code qui doit être nettoyé.'], ['🛂', ':passport_control:', 'Travailler sur le code lié à l'autorisation, aux rôles et aux permissions.'], ['🩹', ':adhesive_bandage:', 'Correction simple pour un problème non critique.'], ['🧐', ':monocle_face:', 'Exploration/inspection des données.'], ['⚰️', ':coffin:', 'Supprimer du code obsolète.'], ['🧪', ':test_tube:', 'Ajouter un test en échec.'], ['👔', ':necktie:', 'Ajouter ou mettre à jour la logique métier.'], ['🩺', ':stethoscope:', 'Ajouter ou mettre à jour le contrôle de santé.'], ['🧱', ':bricks:', 'Modifications liées à l'infrastructure.'], ['🧑‍💻', ':technologist:', 'Améliorer l'expérience des développeurs.'], ['💸', ':money_with_wings:', 'Ajouter des sponsorings ou une infrastructure liée à l'argent.'], ['🧵', ':thread:', 'Ajouter ou mettre à jour le code lié au multithreading ou à la concurrence.'], ['🦺', ':safety_vest:', 'Ajouter ou mettre à jour le code lié à la validation.']]\n\nINSTRUCTION : Tu es un expert en Git Commit Message : Tu reçois des modifications d'un projet et tu génères un message de commit.\nTa réponse doit uniquement être le message de commit, sans superflu.\nLe message de commit doit commencer par le code_emoji (voir doc) puis le message."

# Effacer le terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Afficher un message de démarrage en rouge
print("\033[96mDémarrage de CommitGPT...\033[0m")

# Chemin vers le répertoire du projet Git (emplacement actuel du fichier)
repo_path = os.path.dirname(os.path.abspath(__file__))

# Récupérer le dépôt Git existant
repo = Repo(repo_path)

# Récupérer les fichiers modifiés ajoutés avec git add
modified_files = [item.a_path for item in repo.index.diff("HEAD")]
if not modified_files:
    print("\033[91mAucun fichier modifié n'a été trouvé. Veuillez utiliser git add pour ajouter des fichiers.\033[0m")
    exit()

# Récupérer les différences avant - après pour chaque fichier modifié
diffs = []
for file in modified_files:
    if not os.path.exists(file):
        diff = repo.git.diff("HEAD", file)
        diffs.append(diff)
    else:
        # Récupérer les différences avant - après
        diff_output = repo.git.diff("HEAD", file)
        lines = diff_output.split('\n')
        # Seules les lignes commençant par '+' ou '-' sont conservées, mais on élimine celles qui commencent par '---' ou '+++'
        diffs.append('\n'.join(line for line in lines if line.startswith(('+', '-')) and not line.startswith(('---', '+++'))))

print("\033[92mFichiers modifiés:\033[0m\n" + "\n".join(diffs))

# Générer le résumé des modifications avec GPT-3.5 Turbo
summary_prompt = "\n".join(diffs)
response_summary = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": summary_context},
        {"role": "user", "content": summary_prompt},
    ],
    temperature=0.7,
)
summary_message = response_summary.choices[-1].message.content.strip()

# Afficher le résumé en vert et demander l'approbation de l'utilisateur pour continuer sinon demande le résumé à l'utilisateur.
print("\033[92mRésumé des modifications:\033[0m\n" + summary_message)
user_input = input("Est-ce que le résumé vous convient? (y) Oui, (n) Non")
if user_input == "n":
    summary_message = input("Veuillez entrer un résumé: ")

while True:
    # Générer le message de commit avec GPT-3.5 Turbo en utilisant le résumé et les fichiers modifiés
    commit_prompt = "\n".join(modified_files + [summary_message])
    response_commit = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": commit_context},
            {"role": "user", "content": commit_prompt},
        ],
        temperature=0.7,
    )
    commit_message = response_commit.choices[-1].message.content.strip()

    # Afficher le message de commit et demander l'approbation de l'utilisateur
    print("Message de commit: " + commit_message)
    user_input = input("Est-ce que le message de commit vous convient? (y) Oui, (n) Non, (q) Quitter: ")

    if user_input == "y":
        # Effectuer le commit avec le message généré
        if modified_files:
            repo.git.commit(message=commit_message)
            print("\033[92mCommit effectué avec succès !\033[0m")
        break
    elif user_input == "n":
        # Recommencer la génération
        summary_message = response_summary.choices[-1].message.content.strip()
    elif user_input == "q":
        # Quitter
        break
    else:
        print("Veuillez entrer (c) Commit, (r) Regénérer ou (q) Quitter")