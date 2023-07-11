import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Folder = () => {
    const [folders, setFolders] = useState([]);
    const [newFolderName, setNewFolderName] = useState("");

    useEffect( () => {
        axios.get("http://localhost:8000/api/folders/")
            .then(res => setFolders(res.data));
    }, []);

    const handleInputChange = event => {
        setNewFolderName(event.target.value);
    }

    const handleFormSubmit = event => {
        event.preventDefault();
        axios.post("http://localhost:8000/api/folders/", {name: newFolderName })
            .then(res => setFolders([...folders, res.data]));
        setNewFolderName("");
    }

    return (
        <div>
            <form onSubmit={handleFormSubmit}>
                <input type="text" value={newFolderName} onChange={handleInputChange} required />
                <button type="submit">Create Folder</button>
            </form>
            <ul>
                {folders.map(folder => (
                    <li key={folder.id}>{folder.name}</li>
                ))}
            </ul>
        </div>
    )

}

export default Folder;