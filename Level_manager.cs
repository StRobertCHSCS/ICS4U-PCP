using UnityEngine;
using System.Collections;

public class Level_manager : MonoBehaviour {

    public GameObject current_respawnpoint;

    private NewBehaviourScript scorpion;

	// Use this for initialization
	void Start () {
        scorpion = FindObjectOfType<NewBehaviourScript>();
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

    public void Respawn_Player()
    {
        Debug.Log("Player Respawn");
        scorpion.transform.position = current_respawnpoint.transform.position;
    }
}
