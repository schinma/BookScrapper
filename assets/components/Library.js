import React, { Component } from "react";
import axios from "axios";
import { Table } from 'reactstrap';
import { Navbar, Button, ButtonGroup } from 'reactstrap';
import { InputGroup, Input, } from 'reactstrap';
import BookLine from './Book';
import FileUploader from './FileUploader';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

class ToolBar extends Component {
  constructor(props) {
    super(props);
  }

  uploadFiles = (files) => {

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append("file-"+i, files[i]);
    }
    console.log(formData);
    const config = {
      headers : {
        'content-type' : 'multipart/form-data'
      }
    }
    
    axios.post(URLS.UPLOAD_FILES, formData, config)
    .then(response => {
      console.log(response);
      console.log(response.data);
    });
  }

  render() {
    return (
      <Navbar>
        <ButtonGroup>

          <FileUploader name="Ajouter" handleFiles={this.uploadFiles}/>
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
    );
  }
}

class Library extends Component {
    constructor(props) {
      super(props);
      this.state = {
        book_list: [],
        placeholder: "Loading"
      };
    }
  
    componentDidMount() {
      axios.get(URLS.LIST_BOOKS)
        .then(response => {
          if (response.status > 400) {
            this.setState({ placeholder: "Something went wrong!" });
          } else {
            const book_list = response.data;
            this.setState({ book_list });
          }
          
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
          {this.state.book_list.map(book => {
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