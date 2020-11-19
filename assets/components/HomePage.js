import React, { Component } from "react";
import Library from "./Library";

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