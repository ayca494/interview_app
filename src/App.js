import {useAuth0} from '@auth0/auth0-react'

function App() {
  const {loginWithRedirect, logout, isAuthenticated, isLoading ,user} =useAuth0();

console.log('user', user);

  return (
    <div className="App">
      {isLoading ? <p>Loading...</p> : 
      isAuthenticated ? <button type="button" class="btn btn-primary" onClick={logout}>Logout</button> : <button type="button" class="btn btn-primary" onClick={loginWithRedirect}>Login</button>}           
    
    {isAuthenticated && <div>
      <img src={user.picture} alt={user.name} />
      <h2>{user.name}</h2>
      <p>{user.email}</p>
      </div>}
    </div>
  );
}

export default App;
