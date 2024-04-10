// rasaChatWidget.js

const React = require('react');
const ReactDOM = require('react-dom');

const { Widget } = require('rasa-webchat');

ReactDOM.render(
  <Widget
    initPayload={"/get_started"}
    socketUrl={"http://localhost:5005"}
    socketPath={"/socket.io/"}
    customData={{"language": "en"}}
    title={"Your Rasa Assistant"}
  />,
  document.getElementById('rasa-chat-widget')
);