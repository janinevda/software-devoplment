using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using WebSocketSharp;

public class networkManager : MonoBehaviour
{
    private WebSocket ws;

    public GameObject sl;
    stoplicht stoplicht;

    // Start is called before the first frame update
    public void Start()
    {
        stoplicht = sl.GetComponent<stoplicht>();

        this.ws = new WebSocket("ws://127.0.0.1:1234");
        this.ws.OnOpen += (sender, e) =>
        {
            Debug.Log("opened");
        };
        this.ws.OnMessage += (sender, e) =>
        {
            Debug.Log(e.Data);

            if (e.Data == "0")
            {
                Debug.Log('0');
                this.ws.Send("status set to 0");
                stoplicht.status = 0;
            }
            else if (e.Data == "1")
            {
                Debug.Log(1);
                this.ws.Send("status set to 1");
                stoplicht.status = 1;
            }
        };
        this.ws.Connect();
    }

    public void Open()
    {

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
