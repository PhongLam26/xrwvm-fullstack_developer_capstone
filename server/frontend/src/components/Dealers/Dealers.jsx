import React, {useEffect,useState} from "react";
import {Link,useSearchParams} from "react-router-dom";
import Header from "../Header/Header";
export default function Dealers(){
 const [dealers,setDealers]=useState([]),[states,setStates]=useState([]),[error,setError]=useState("");
 const [params,setParams]=useSearchParams(); const state=params.get("state")||"";
 const logged=!!sessionStorage.getItem("username");
 useEffect(()=>{fetch("/djangoapp/get_dealers").then(r=>r.json()).then(d=>setStates([...new Set(d.dealers.map(x=>x.state))].sort())).catch(e=>setError(e.message));},[]);
 useEffect(()=>{fetch("/djangoapp/get_dealers"+(state?"/"+encodeURIComponent(state):"")).then(r=>r.json()).then(d=>{if(d.error)throw Error(d.error);setDealers(d.dealers);}).catch(e=>setError(e.message));},[state]);
 return <><Header/><main className="page-shell"><p className="eyebrow">Find your next destination</p><h1>Explore our dealerships</h1><p className="muted">Browse 50 dealerships and read experiences shared by drivers.</p><label htmlFor="state">Filter by State</label><select id="state" value={state} onChange={e=>setParams(e.target.value?{state:e.target.value}:{})}><option value="">All States</option>{states.map(s=><option key={s}>{s}</option>)}</select>{error&&<p role="alert">{error}</p>}<p>{dealers.length} dealerships found</p><div className="table-scroll"><table><thead><tr><th>ID</th><th>Dealer Name</th><th>City</th><th>Address</th><th>Zip</th><th>State</th>{logged&&<th>Review Dealer</th>}</tr></thead><tbody>{dealers.map(d=><tr key={d.id}><td>{d.id}</td><td><Link to={"/dealer/"+d.id}>{d.full_name}</Link></td><td>{d.city}</td><td>{d.address}</td><td>{d.zip}</td><td>{d.state}</td>{logged&&<td><Link to={"/postreview/"+d.id}>Review Dealer</Link></td>}</tr>)}</tbody></table></div></main></>;
}