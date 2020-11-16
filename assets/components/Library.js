import React, { Component } from "react";
import { Table } from 'reactstrap';
import AuthorModal from './Author'

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
        <Table>
          <thead>
            <tr>
              <th>#</th>
              <th>Titre</th>
              <th>Auteur</th>
            </tr>
          </thead>
          <tbody>
          {this.state.data.map(book => {
            return (
              <tr key={book.id}>
                <th scope='row'>{book.id}</th>
                <td>{book.title}</td>
                <td><AuthorModal firstName={book.author.first_name} lastName={book.author.last_name}/></td>
              </tr>
            );
          })}
          </tbody>
        </Table>
      );
    }
}

export default Library;