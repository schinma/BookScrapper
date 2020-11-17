import React, { Component } from "react";
import AuthorModal from "./Author";
import {  
    Row, Col, Button, 
    Modal, ModalBody,
    Card, CardBody, CardTitle, CardText } from 'reactstrap';

class BookEditModal extends Component {
    constructor(props) {
        super(props);
        this.state = {
            moda: false,
        }
    }

    toggle = () => {
        this.setState({
            modal : !this.state.modal,
        });
    }

    render() {
        return (
            <div>
                <Button onClick={this.toggle}>Editer</Button>
                <Modal isOpen={this.state.modal} toggle={this.toggle}>
                    <ModalBody>
                    <Card>
                        <Row className='no-gutters'>
                            <Col sm='5'>
                                <img src="images/sample.svg" className="card-img-top h-100" alt="..."/>
                            </Col>
                            <Col sm='7'>
                                <CardBody>
                                    <CardTitle><h5>{this.props.title}</h5></CardTitle>
                                    <CardText>
                                        {this.props.firstName} , {this.props.lastName}
                                    </CardText>
                                    <CardText>
                                        {this.props.serie}, {this.props.serieNumber}
                                    </CardText>
                                    <CardText>
                                        {this.props.synopsis}
                                    </CardText>
                                </CardBody>
                            </Col>
                        </Row>
                    </Card>
                    </ModalBody>
                </Modal>
            </div>
        )

    }
}

class BookLine extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <tr>
                <th scope='row'>{this.props.id}</th>
                <td>{this.props.title}</td>
                <td><AuthorModal firstName={this.props.firstName} lastName={this.props.lastName}/></td>
                <td>{this.props.serie} [{this.props.serieNumber}]</td>
                <td>{this.props.dateAdded}</td>
                <td>{this.props.read}</td>
                <td>{this.props.dateRead ? this.props.dateRead : "Pas encore lu"}</td>
                <td><BookEditModal {...this.props} /></td>
              </tr>
        );
    }
}

export default BookLine;