import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Link, Route, Redirect } from 'react-router-dom';

class HomePage extends Component{
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <main>
                <h1>HomePage</h1>
                <p>
                    This is the Homepage !
                </p>
            </main>
        );
    }
}

export default HomePage;