using UnityEngine;
using System.Collections;

public class LevelManager2 : MonoBehaviour
{

    public GameObject currentCheckpoint2;

    private MarioController player;

    // Use this for initialization
    void Start()
    {
        player = FindObjectOfType<MarioController>();

    }

    // Update is called once per frame
    void Update()
    {

    }

    public void RespawnPlayer()
    {
        Debug.Log("Player Respawn");
        //player.transform. = new Vector2(0, GetComponent<Rigidbody2D>().velocity.y);
        player.transform.position = currentCheckpoint2.transform.position;
    }
}

