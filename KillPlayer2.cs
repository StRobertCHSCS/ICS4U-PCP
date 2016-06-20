using UnityEngine;
using System.Collections;

public class KillPlayer2 : MonoBehaviour
{

    public LevelManager2 levelManager2;

    // Use this for initialization
    void Start()
    {
        levelManager2 = FindObjectOfType<LevelManager2>();
    }

    // Update is called once per frame
    void Update()
    {

    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.name == "mario2")
        {
            levelManager2.RespawnPlayer();
        }
    }
}