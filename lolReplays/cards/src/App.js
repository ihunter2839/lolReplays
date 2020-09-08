import React, { Component }  from 'react';
import { 
    BrowserRouter as Router, 
    Switch,
    Route,
    Link
} from 'react-router-dom';
import './App.css';

class App extends Component {

    constructor(props) {
        super(props);

        this.state = {
            ws: null,
            message: '',
        };
    }

    componentDidMount() {
        var ws = new WebSocket(
            "ws://"
            + window.location.host
            + "/ws/chat/room/"
        );

        ws.onmessage = (e) => {
            console.log(e);
        };

        ws.onclose = () => {
            console.log("ws closed");
        };

        this.setState({
            ws: ws
        });
    }

    //const [room, setRoom] = useState('');
    //const [message, setMessage] = useState('');
    //const [messages, setMessages] = useState([]);
    //const [chatSocket, setChatSocket] = useState(new WebSocket(
    //    "ws://"
    //    + window.location.host
    //    + "/ws/chat/room/"
    //));

    /*useEffect( () => {
        console.log("initializing websocket");
        chatSocket.onmessage = function(e) {
            console.log(e);
            setMessages([...messages, JSON.parse(e.data)]);
        };

        chatSocket.onclose = function(e) {
            console.log("socket closed unexpectedly");
        };
    }, []);
    */

    render() {
        return (
            <Router>
                <div className="App">
                    <Switch>
                        <Route path="/cards" exact>
                            <p> select chat room </p> 
                            <input 
                                id="room-name-input" 
                                type="text"
                            />
                            <input 
                                id="room-name-submit" 
                                type="button" 
                                value="Enter"
                                onClick={ () => window.location.pathname = "/cards/room/" }
                            />
                        </Route>
                        <Route path="/cards/room">
                            <p> welcome to the room </p>
                            <textarea
                                value={this.state.message}
                                onChange={ (e) => this.setState({
                                    message: e.target.value,
                                })}>
                            </textarea>
                            <button
                                type="button"
                                onClick={ () => {
                                console.log('sending websocket message');
                                this.state.ws.send(JSON.stringify({
                                    'message': this.state.message
                                }))}}>
                                Send
                            </button>
                        </Route>
                    </Switch>
                </div>
            </Router>
        );
    }
}

export default App;
