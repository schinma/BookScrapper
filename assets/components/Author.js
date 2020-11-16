import React, { Component } from "react";
import {  Button, Modal, ModalBody, ModalFooter, ModalHeader } from 'reactstrap';

class AuthorModal  extends Component {
    constructor(props) {
        super(props);
        this.state = {
            modal : false,   
            bio : "No bio registered yet !",
            website : "No website registered yet !"
        }
        this.toggle = this.toggle.bind(this);
    }

    toggle(){
        this.setState({
            modal : !this.state.modal,
        });
    }

    render() {
        return (
            <div>
                <Button onClick={this.toggle}>{this.props.firstName} {this.props.lastName}</Button>
                <Modal isOpen={this.state.modal} toggle={this.toggle} className={this.props.className}>
                    <ModalHeader>{this.props.firstName} {this.props.lastName}</ModalHeader>
                    <ModalBody>
                        <h5>Bio</h5>
                        <p>{this.state.bio}</p>
                        <a href={this.state.website}>{this.state.website}</a>
                    <ModalFooter>
                        <Button color='secondary' onClick={this.toggle}>Close</Button>
                    </ModalFooter>
                    </ModalBody>
                </Modal>
            </div>
        );
    }
}

export default AuthorModal;