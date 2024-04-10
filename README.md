# Étape

# Mise à jour du code

- Création d'un fichier HTML
- Création d'un fichier js
- Modification du fichier credentials.yml

# Intégration du modèle RASA dans le site web

Si l'API Rasa fonctionne correctement, on intégre le widget de chat dans le site Web.  
**rasaChatwidget.js** & **index.html** 

1. il faut assurer que `index.html` est accessible sur le site Web 
il faut le placer dans le répertoire racine du serveur Web

Pareil pour`rasaChatWidget.js` le placer dans un sous-répertoire du serveur Web, par exemple `js/`

3. Mettre à jour le chemin vers le fichier `rasaChatWidget.js` dans lefichier HTML. 
Exemple, si on a placé `rasaChatWidget.js` dans un sous-répertoire `js/`, il faut à jour la balise script dans le fichier HTML :

```html
<script src="js/rasaChatWidget.js"></script>
```

4. Ouvrez votre fichier HTML dans un navigateur. Vous devriez voir le widget de chat Rasa sur votre page.

5. Tester le widget de chat en envoyant un message (normalement on peut avoir un message du bot Rasa

S'il y a des problèmes, on vérifie :

- Le serveur Rasa est-il en cours d'exécution ?
- L'URL du serveur Rasa dans le fichier js est correcte ? (normalement est bon)
- Le fichier js est correctement lié dans le fichier HTML ?
- Le navigateur autorise des scripts js à s'exécuter ?
