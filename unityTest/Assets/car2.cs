using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class car2 : MonoBehaviour
{
    public List<GameObject> path;
    private int currentTarget = 0;

    public NavMeshAgent agent;

    public bool mayMove = true;

    // Start is called before the first frame update
    void Start()
    {
        agent.SetDestination(path[currentTarget].transform.position);
    }

    // Update is called once per frame
    void Update()
    {
        Debug.DrawRay(transform.position + new Vector3(0f, 0.125f, 0f), transform.TransformDirection(Vector3.forward), Color.red);
        //agent.SetDestination(transform.position);
        agent.isStopped = true;

        int layerMask = 1 << 11;
        //layerMask = ~layerMask;
        RaycastHit hit;

        if (Physics.Raycast(transform.position + new Vector3(0f, 0.125f, 0f), transform.TransformDirection(Vector3.forward), 0.75f, layerMask, QueryTriggerInteraction.Ignore))
        {
            Debug.Log("test");
        }

        if (mayMove)
        {
            agent.isStopped = false;
            //agent.SetDestination(path[currentTarget].transform.position);
            if (Vector3.Distance(transform.position, path[currentTarget].transform.position) <= 0.25f)
            {
                if (path.Count > currentTarget + 1)
                {
                    currentTarget++;
                    agent.SetDestination(path[currentTarget].transform.position);
                }
                else
                {
                    Destroy(this.gameObject);
                }
            }
        }
    }

    private void OnTriggerStay(Collider other)
    {
        int status = other.GetComponentInParent<stoplicht>().status;

        if (status == 0)
        {
            mayMove = false;
        }
        else if (status == 1)
        {
            mayMove = true;
        }
    }
}
