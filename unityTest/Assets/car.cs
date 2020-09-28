using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class car : MonoBehaviour
{
    private List<GameObject> path = new List<GameObject>();
    private int currentTarget = 0;
    public GameObject stoplicht;

    public Material red;
    public Material green;

    RaycastHit hit;

    // Start is called before the first frame update
    void Start()
    {
        if (Physics.Raycast(transform.position, Vector3.down, out hit))
        {
            Debug.Log("hit");

            road Road = hit.transform.gameObject.GetComponent(typeof(road)) as road;
            int rnd = UnityEngine.Random.Range(0, Road.possibleDirections - 1);

            Debug.Log(rnd);

            if (rnd == 0)
            {
                path = Road.path1;
            }

            stoplicht = hit.transform.gameObject.GetComponent<road>().stoplicht[0];
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (stoplicht.GetComponent<Renderer>().sharedMaterial == green)
        {
            if (Vector3.Distance(transform.position, path[currentTarget].transform.position) > 0.25f)
            {
                float speed = 1f * Time.deltaTime;
                transform.position = Vector3.MoveTowards(transform.position, path[currentTarget].transform.position, speed);
            }
            else
            {
                if (path.Count > currentTarget + 1)
                {
                    currentTarget++;
                }
                else
                {
                    Destroy(this.gameObject);
                }
            }
        }
    }
}
