using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class road : MonoBehaviour
{
    public int possibleDirections = 0;
    [SerializeField] public List<GameObject> path1;
    [SerializeField] public List<GameObject> path2;
    [SerializeField] public List<GameObject> path3;
    [SerializeField] public List<GameObject> path4;
    [SerializeField] public List<GameObject> stoplicht;

    // Start is called before the first frame update
    void Start()
    {
        if (path1.Count != 0)
        {
            possibleDirections++;
        }
        if (path2.Count != 0)
        {
            possibleDirections++;
        }
        if (path3.Count != 0)
        {
            possibleDirections++;
        }
        if (path4.Count != 0)
        {
            possibleDirections++;
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
