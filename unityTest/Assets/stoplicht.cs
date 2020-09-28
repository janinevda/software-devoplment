using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class stoplicht : MonoBehaviour
{
    public GameObject Stoplicht;
    Renderer sl;
    public Material green;
    public Material red;

    public int status = 0;

    float timer = 5f;
    float time = 0;

    // Start is called before the first frame update
    void Start()
    {
        sl = Stoplicht.GetComponent<Renderer>();
    }

    //Update is called once per frame
    void Update()
    {
        //if (time <= 0)
        //{
        //    time = timer;
            if (status == 0)
            {
                sl.material = red;
            }
            else if (status == 1)
            {
                sl.material = green;
            }
        //}
        //else
        //{
        //    time -= Time.deltaTime;
        //}
    }
}
