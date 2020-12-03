import React, { Component } from "react";
import { Button } from 'reactstrap';

class FileUploader extends Component{
    constructor(props) {
        super(props);
        this.state = {
            files : [],
        }
        this.hiddenFileInput = React.createRef();
    }

    handleChange = (event) => {
        const files = event.target.files;
        this.props.handleFiles(files);
    }

    handleClick = () => {
        this.hiddenFileInput.current.click();
    }

    render() {
        return (
            <div className="file-uploader">
                <input
                    type="file"
                    ref={this.hiddenFileInput}
                    style={{display:'none'}}
                    onChange={this.handleChange}
                    multiple
                />
                <Button onClick={this.handleClick}>
                    {this.props.name}
                </Button>
          </div>
        );
    }
}

export default FileUploader;
