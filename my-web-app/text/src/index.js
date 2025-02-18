const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(cors());

app.get('/api/items', async (req, res) => {
    try {
        const response = await axios.get('http://backend:8000/api/items/');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Backend not reachable' });
    }
});

app.listen(3000, () => console.log('Frontend running on port 3000'));
