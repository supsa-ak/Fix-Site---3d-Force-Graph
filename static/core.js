class NodeCore {
    constructor() {
        this.window = window;
    };
    onNodeClick = async (node) => {
        // console.log("node was clicked: ",node);
        // console.log(node['id']);

        document.getElementById("heading_current_node").style.display = "initial";
        document.getElementById("create_new_node_btn").style.display = "initial";
        document.getElementById("update_node").style.display = "initial";
        document.getElementById("connected_to_div").style.display = "initial";
        document.getElementById("conn-to-label").style.display = "initial";
        document.getElementById("nodeconn").innerHTML = "";
        document.getElementById("nodeconn2").innerHTML = "";
        document.getElementById("form").action = "/updatenode";

        if (document.getElementById("submit-create-new-node")) {
            document.getElementById("submit-create-new-node").remove();
            document.getElementById("heading_new_node_h3").remove();
        }
        document.getElementById('nodeid').value = node['id'];
        document.getElementById('nodedesc').value = node['description'];
        document.getElementById('nodegrp').value = node['group'];
        var link_no = node['links'].length;

        for (let i = 0; i < link_no; i++) {
            var element = document.createElement("option");
            element.appendChild(document.createTextNode(node['links'][i]['target']));
            element.value = node['links'][i]['target'];
            element.selected = true;
            document.getElementById('nodeconn').appendChild(element);
        }
        // console.log('prev', all_nodes);


        let rem_array = []
        for (let i = 0; i < link_no; i++) {
            rem_array.push(node['links'][i]['target']);
        }
        rem_array.push(node['id']);
        
        // console.log('this is rem-arr', rem_array);
        var diff = $(all_nodes).not(rem_array).get();

        for (let i = 0; i < diff.length; i++) {
            var element = document.createElement("option");
            element.appendChild(document.createTextNode(diff[i]));
            element.value = diff[i];
            document.getElementById('nodeconn2').appendChild(element);
        }

        // console.log('this is diff', diff);
        // console.log("after all ", all_nodes);
    };
}

function create_new_node() {

    document.getElementById('nodeid').value = "";
    document.getElementById('nodedesc').value = "";
    document.getElementById('nodegrp').value = "";

    document.getElementById("heading_current_node").style.display = "none";
    document.getElementById("create_new_node_btn").style.display = "none";
    document.getElementById("update_node").style.display = "none";
    document.getElementById("connected_to_div").style.display = "none";
    document.getElementById("conn-to-label").style.display = "none";

    document.getElementById("nodeconn").innerHTML = "";
    document.getElementById("nodeconn2").innerHTML = "";

    document.getElementById("form").action = "/createnewnode";

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
    tag.id = "heading_new_node_h3";
    var element = document.getElementById("heading_new_node");
    element.appendChild(tag);

    for (let i = 0; i < all_nodes.length; i++) {
        var element = document.createElement("option");
        element.appendChild(document.createTextNode(all_nodes[i]));
        element.value = all_nodes[i];
        document.getElementById('nodeconn2').appendChild(element);
    }
}