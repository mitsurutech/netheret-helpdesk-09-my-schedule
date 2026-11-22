# Centre d'assistance Netheret, étape 09 : mon planning

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un exemple pour enseigner. En seize étapes, nous construisons une application web de centre d'assistance pour Netheret, une entreprise imaginaire qui s'occupe de l'informatique de petites entreprises. Cette étape donne aux ingénieurs Tier 2 et Tier 3 leur propre planning et une fiche pour chaque intervention, où ils indiquent leur avancement.

## Ce que cette étape ajoute

Dans `helpdesk/jobs.py` :

- `/jobs/mine` : les interventions d'un ingénieur à partir d'aujourd'hui, regroupées par jour, plus
  toute intervention plus ancienne encore marquée « in progress ».
- `/jobs/<id>` : la fiche d'intervention : quand, où, le numéro de téléphone du client, la
  consigne et, si l'intervention vient d'une demande, le problème d'origine du client.
- `/jobs/<id>/progress` : l'ingénieur passe l'intervention à « in progress » ou
  « done » et écrit des notes. Quand une intervention issue d'une demande est terminée, une note s'ajoute
  au fil chronologique de cette demande.

Dans `helpdesk/models.py`, `Job.can_be_seen_by()` et `Job.can_be_updated_by()`
gardent en un seul endroit les règles qui disent qui peut voir et modifier une intervention. La vue
de la semaine et la page de la fiche s'en servent toutes les deux.

## Lancer l'application

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Connectez-vous en tant que `tier2@netheret.example` ou `tier3@netheret.example` (mot de passe de
démonstration `password123`) et ouvrez My schedule. Essayez d'ouvrir l'intervention d'un autre
ingénieur depuis la vue de la semaine : il n'y a pas de lien, et taper l'adresse
donne 403.

## À regarder

- `days.setdefault(day, []).append(job)` : une façon courte de regrouper une liste en
  dictionnaire de listes.
- Un ingénieur ne peut pas annuler une intervention. Le formulaire ne propose pas ce choix, et le
  serveur le refuse aussi, car la personne qui utilise un formulaire peut le modifier.
- `finished_now` : la note du fil chronologique n'est écrite que la première fois qu'une intervention
  passe à terminée, pas à chaque enregistrement des notes.

## Apprendre cette étape

Voici l'étape 9 sur 16 de **Task 2. Developing the solution**, une série gratuite de leçons de T Level Digital Software Development, en anglais, qui construit le centre d'assistance Netheret en sprints agiles avec Python et Flask. Lisez la leçon de cette étape :
[Le planning d'un ingénieur et les fiches d'intervention](https://mitsurutech.co.uk/resources/t-level/dsd-t2-09-my-schedule).

- Étape précédente : [étape 08, planifier des interventions sur site](https://github.com/mitsurutech/netheret-helpdesk-08-jobs)
- Étape suivante : [étape 10, la base de connaissances](https://github.com/mitsurutech/netheret-helpdesk-10-knowledge-base)
- [Toutes les leçons gratuites de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseigner ces leçons à votre classe sur MitsuruTech](https://mitsurutech.co.uk/fr/learning), [voir les tarifs](https://mitsurutech.co.uk/fr/pricing) ou
  [commencer une année gratuite pour votre établissement](https://mitsurutech.co.uk/fr/signup)

## À propos

Écrit par [Mitsuru Technologies](https://mitsurutech.co.uk/fr) (MitsuruTech) comme exemple pédagogique pour le T Level Digital
Software Development. Le cahier des charges Netheret IT Support Solutions provient du matériel d'évaluation type de Pearson ; ce code
et ses notes sont les nôtres, et ne sont ni publiés, ni soutenus, ni approuvés par Pearson ou le Department for Education.
« T Level » est une marque déposée du Department for Education.
