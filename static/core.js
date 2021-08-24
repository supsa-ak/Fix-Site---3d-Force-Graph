class NodeCore {
    constructor() {
        this.window = window;
    };
    onNodeClick = async (node)=>{
        // console.log("node was clicked: ",node);
        // console.log(node['id']);

        document.getElementById("heading_current_node").style.display = "initial";
        document.getElementById("create_new_node_btn").style.display = "initial";
        document.getElementById("update_node").style.display = "initial";
        if(document.getElementById("submit-create-new-node")){
            document.getElementById("submit-create-new-node").remove();
            document.getElementById("heading_new_node").remove();
        }
        document.getElementById('nodeid').value = node['id']; 
        document.getElementById('nodedesc').value = node['description']; 
        document.getElementById('nodegrp').value = node['group']; 
        document.getElementById('nodeconn').value =  " ";
        var link_no = node['links'].length
        for(let i=0; i<link_no; i++){
            document.getElementById('nodeconn').value += node['links'][i]['target'] + " ";
        }
    };
}

function create_new_node(){

    document.getElementById('nodeid').value = ""; 
    document.getElementById('nodedesc').value = ""; 
    document.getElementById('nodegrp').value = ""; 
    document.getElementById('nodeconn').value = "";

    document.getElementById("heading_current_node").style.display = "none";
    document.getElementById("create_new_node_btn").style.display = "none";
    document.getElementById("update_node").style.display = "none";
    var tag = document.createElement("button");
    tag.className = "btn btn-light";
    tag.type = "submit";
    tag.id = "submit-create-new-node";
    var text = document.createTextNode("Create");
    tag.appendChild(text);
    var element = document.getElementById("create-btn");
    element.appendChild(tag);
   
    var tag = document.createElement("h3");
    var text = document.createTextNode("New Node");
    tag.appendChild(text);
    var element = document.getElementById("heading_new_node");
    element.appendChild(tag);
}
