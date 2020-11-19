import React, { Component } from "react";
import { Table } from 'reactstrap';
import { Navbar, Button, ButtonGroup } from 'reactstrap';
import { InputGroup, InputGroupAddon, Input, InputGroupText } from 'reactstrap';
import BookLine from './Book';


class ToolBar extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Navbar>
        <ButtonGroup>
          <Button>Ajouter</Button>
          <Button>Editer</Button>
          <Button>Convertir</Button>
          <Button>Download</Button>      
        </ButtonGroup>
      </Navbar>
    );
  }
}

class SearchBar extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <InputGroup>
        <Input placeholder="search"/>
      </InputGroup>
    )
  }
}

class Library extends Component {
    constructor(props) {
      super(props);
      this.state = {
        data: [],
        loaded: false,
        placeholder: "Loading"
      };
    }
  
    componentDidMount() {
      fetch(URLS.LIST_BOOKS)
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(data => {
          this.setState(() => {
            return {
              data,
              loaded: true
            };
          });
        });
    }
  
    render() {
      return (
        <div>
        <ToolBar/>
        <SearchBar/>
        <Table>
          <thead>
            <tr>
              <th>#</th>
              <th>Titre</th>
              <th>Auteur</th>
              <th>Série</th>
              <th>Date</th>
              <th>Lu</th>
              <th>Date Lu</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
          {this.state.data.map(book => {
            return ( 
            <BookLine key={book.id}
              id={book.id} 
              title={book.title} 
              firstName={book.author.first_name} 
              lastName={book.author.last_name}
              serie={book.serie}
              serieNumber={book.serie_number}
              dateAdded={book.date_added}
              read={book.read}
              dateRead={book.date_read}
            />
            );
          })}
          </tbody>
        </Table>
        </div>
      );
    }
}

export default Library;