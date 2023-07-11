import React, { useState, useEffect } from 'react';
import axios from 'axios';

const File = () => {
    const [folders, setFolders] = useState([]);
    const [selectedFolder, setSelectedFolder] = useState("");
    const [selectedFile, setSelectedFile] = useState(null);
    const [files, setFiles] = useState([]);
    const [newFileName, setNewFileName] = useState("");

    useEffect(() => {
        // fetch all folders when the component is mounted
        axios.get('http://localhost:8000/api/folders/')
            .then(response => {
                setFolders(response.data);
                if (response.data.length > 0) {
                    setSelectedFolder(response.data[0].id.toString());
                }
            })
            .catch(error => {
                console.log(error);
            });

        // fetch all files when the component is mounted
        axios.get('http://localhost:8000/api/files/')
            .then(response => {
                setFiles(response.data);
            })
            .catch(error => {
                console.log(error);
            });
    }, []);

    const handleInputChange = event => {
        setNewFileName(event.target.value);
    }

    const handleFileChange = event => {
        setSelectedFile(event.target.files[0]);
    };


    const handleFolderChange = event => {
        setSelectedFolder(event.target.value);
    };

    const handleFileUpload = event => {
        event.preventDefault()

        const formData = new FormData();

        formData.append('name', newFileName);
        formData.append('file', selectedFile);
        formData.append('parent_folder', selectedFolder);

        axios.post('http://localhost:8000/api/files/', formData, {
            headers: {
                'content-type': 'multipart/form-data'
            }
        }).then(response => {
            console.log(response.data);
            // refresh the list of files
            axios.get('http://localhost:8000/api/files/')
                .then(response => {
                    setFiles(response.data);
                })
                .catch(error => {
                    console.log(error);
                });
        }).catch(error => {
            console.log(error);
        });
        setNewFileName("");
    };

    const filesInSelectedFolder = files.filter(file => file.parent_folder === Number(selectedFolder));

    return (
        <div>
            <select value={selectedFolder} onChange={handleFolderChange}>
                {folders.map(folder => (
                    <option key={folder.id} value={folder.id}>{folder.name}</option>
                ))}
            </select>
            <form onSubmit={handleFileUpload}>
                <input type="file" onChange={handleFileChange} />
                <input type="text" value={newFileName} onChange={handleInputChange} required />
                <button type="submit">Upload File</button>
            </form>

            <ul>
                {filesInSelectedFolder.map(file => (
                    <li key={file.id}>{file.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default File;
