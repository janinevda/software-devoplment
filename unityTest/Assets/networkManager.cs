using System.Collections;
using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using WebSocketSharp;
using System.Web;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class networkManager : MonoBehaviour
{
    private WebSocket ws;

    public GameObject sl;
    stoplicht stoplicht;

    public float timerMax = 1f;
    public float timer = 0;

    public string message;
    public bool newMessage = false;

    Socket sender;

    // Start is called before the first frame update
    public void Start()
    {
        stoplicht = sl.GetComponent<stoplicht>();



        try
        {
            IPAddress ipAddr = IPAddress.Parse("127.0.0.1");
            IPEndPoint localEndPoint = new IPEndPoint(ipAddr, 54000);

            sender = new Socket(ipAddr.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            sender.Connect(localEndPoint);

            Debug.Log("Socket connected to -> {0} " + sender.RemoteEndPoint.ToString());

        }
        catch
        {
            Debug.Log("failed");
        }

        StartCoroutine("proccesMessage");

        //this.ws = new WebSocket("ws://127.0.0.1:54000");
        //this.ws.OnOpen += (sender, e) =>
        //{
        //    Debug.Log("connected");
        //};
        //this.ws.OnMessage += (sender, e) =>
        //{
        //    try
        //    {
        //        Debug.Log(e.Data);
                
        //        message = e.Data;
        //        newMessage = true;
        //    }
        //    catch
        //    {
        //        Debug.Log("invalid message");
        //    }
        //};
        //this.ws.Connect();
    }

    public void Open()
    {

    }

    string formatHeader(string message)
    {
        string x = message.Length.ToString() + ':' + message;
        return x;
    }

    IEnumerator proccesMessage()
    {
        while (true)
        {
            if (newMessage)
            {
                newMessage = false;

                var splitString = message.Split(new[] { ':' }, 2);
                if (splitString[1].Length == Convert.ToInt32(splitString[0]))
                {
                    JObject jobj = JObject.Parse(splitString[1]);
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
                else
                {
                    Debug.Log("invallid message");
                    Debug.Log(splitString[1].Length);
                    Debug.Log(splitString[1]);
                    Debug.Log(Convert.ToInt32(splitString[0]));
                }
            }

            yield return new WaitForSeconds(0.1f);
        }
    }

    //Update is called once per frame
    void Update()
    {
        //if (!this.ws.IsConnected)
        //{
        //    this.ws.Connect();
        //}
        if (timer <= 0)
        {
            sender.Send(Encoding.UTF8.GetBytes(formatHeader(jason.instance.jobj.ToString())));

            byte[] messageReceived = new byte[1024];

            int byteRecv = sender.Receive(messageReceived);
            //Debug.Log("Message from Server -> {0} " + Encoding.UTF8.GetString(messageReceived, 0, byteRecv));
            message = Encoding.UTF8.GetString(messageReceived, 0, byteRecv);
            Debug.Log("message received");
            Debug.Log(message);
            newMessage = true;

            //this.ws.Send(formatHeader(jason.instance.jobj.ToString()));
            timer = timerMax;
        }
        else
        {
            timer -= Time.deltaTime;
        }
    }
}
