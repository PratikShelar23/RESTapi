export const getPosts = async() => {
   const response = await fetch('http://localhost:8000/api/companies/', {
        method: 'GET',
    });
    return await response.json();
}