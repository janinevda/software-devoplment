using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using WebSocketSharp;
using System.Web;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

public class networkManager : MonoBehaviour
{
    private WebSocket ws;

    public GameObject sl;
    stoplicht stoplicht;

    

    public string message;
    public bool newMessage = false;

    // Start is called before the first frame update
    public void Start()
    {
        stoplicht = sl.GetComponent<stoplicht>();

        this.ws = new WebSocket("ws://127.0.0.1:54000");
        this.ws.OnOpen += (sender, e) =>
        {
            Debug.Log("opened");
        };
        this.ws.OnMessage += (sender, e) =>
        {
            Debug.Log(e.Data);
            this.ws.Send(jason.instance.jobj.ToString());

            message = e.Data;
            newMessage = true;
        };
        this.ws.Connect();
    }

    public void Open()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (newMessage)
        {
            newMessage = false;

            JObject jobj = JObject.Parse(message);
            Debug.Log(jobj["A1-1"]);

            if (jobj["A1-1"].ToString() == "0")
            {
                Debug.Log('0');
                stoplicht.status = 0;
            }
            else if (jobj["A1-1"].ToString() == "1")
            {
                Debug.Log(1);
                stoplicht.status = 1;
            }
        }
    }
}
